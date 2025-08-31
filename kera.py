"""
AUTHOR  : Carston Wiebe
DATE    : AUG 28 2025
SHORT   : Fill template files with structured data
USAGE   : kera [-h] [--out-dir OUT_DIR] PLATE_FILES... DATA_FILES...
EXAMPLE : kera procedure1.sql.plate procedure2.sql.plate table1.json table2.yml
"""

from enum import Flag, auto
from pathlib import Path
import argparse
import json
import sys
import yaml  # From PyYAML

# Return codes
RETCODE_OK = 0  # Successful execution
RETCODE_NOCREATE_OUTDIR = 1  # Unable to create or find the given output directory

OUT_FILE_KEY = "_out_file"  # When present in a data file, this value is used as the output filename

class Position(Flag):
    """
    The position of the program in a file.  Not an *index* --- rather, this is
    more akin to the "state" of the program.
    """
    IDLE = auto()  # The default
    ESCAPED = auto()  # Escape the next character if it is a "#"
    HASH = auto()  # One "#" has been seen
    SLOT = auto()  # Two "#"s have been seen
    KEY = auto()  # Inside a key in a slot
    END_HASH = auto()  # One "#" has been seen after a slot
    CONDITION_KEY_START = auto()  # A bracket has been seen starting a slot
    CONDITION_KEY = auto()  # Inside a key in a slot condition
    CONDITION_KEY_CLOSE = auto()  # After a key in a slot condition
    CONDITION_KEY_AFTER = auto()  # After a slot condition
    CONDITION_BODY_START = auto()  # One "{" has been seen after a slot condition
    CONDITION_BODY = auto()  # Two "{"s have been seen after a slot condition
    CONDITION_BODY_AFTER = auto()  # After a slot condition body
    CONDITION_FALLBACK_START = auto()  # One "{" has been seen after a slot condition body
    CONDITION_FALLBACK = auto()  # Two "{"s have been seen after a slot condition body
    COLLECTION_BODY_START = auto()  # One "{" has been seen after a key or a join string
    COLLECTION_BODY = auto()  # Two "{"s have been seen after a key or a join string
    COLLECTION_JOIN = auto()  # Inside a join string
    COLLECTION_JOIN_AFTER = auto()  # After a join string

VALID_KEY_CHARS = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-_."
WHITESPACE_CHARS = " \t\n"

def resolve_key(data, key):
    """
    Returns the value of the key as found within the data.  If no record
    exists, returns an empty string.  Uses dot notation to get keys within
    keys.
    """
    parent_and_child = key.split(".", 2)

    if len(parent_and_child) == 2:
        [parent, child] = parent_and_child

        if parent in data:
            return resolve_key(data[parent], child)

        return ""

    if key in data:
        return data[key] if data[key] is not None else ""

    return ""

def trim_body(body):
    """
    Returns the given body with trimmed whitespace.
    """
    start_index = 0
    end_index = len(body) - 1

    def safe():
        """
        Returns whether or not the start index and end index are valid values.
        """
        return start_index < len(body) and end_index > -1

    while safe() and body[start_index] in WHITESPACE_CHARS:
        start_index += 1

    while safe() and body[end_index] in WHITESPACE_CHARS:
        end_index -= 1

    return body[start_index:end_index+1]

def get_body_end(plate, start_index):
    """
    Returns the index of the end of the slot body that starts at the given
    start index.  The returned index is exclusive, and if there is no end
    found for the given body, returns -1.
    """
    num_open = 0
    i = start_index

    while i < len(plate):
        if i == len(plate) - 1:
            return -1

        if plate[i:i+2] == "}}":
            if num_open == 0:
                return i

            num_open -= 1
            i += 1
        elif plate[i:i+2] == "{{":
            num_open += 1
            i += 1

        i += 1

def process(plate, data):
    """
    Process the given string template using the given data.  Returns the
    populated template.
    """
    i = 0  # The current index inside the template
    buffer = ""  # The populated template, built character-by-character
    key = ""  # The current key, as read from the template
    join_str = "\n"  # The current join string, as read from the template.  Defaults to a newline
    condition_status = True  # The status of the current slot condition
    current_position = Position.IDLE  # The current position in the template

    def reprocess():
        """
        Backtracks by one character and sets the current position to idle.
        """
        nonlocal i, current_position
        i -= 1
        current_position = Position.IDLE

    while i < len(plate):
        char = plate[i]

        match current_position:
            case Position.IDLE:
                if char == "#":
                    current_position = Position.HASH
                elif char == "\\":
                    current_position = Position.ESCAPED
                else:
                    buffer += char

            case Position.ESCAPED:
                if char != "#":
                    buffer += "\\"
                buffer += char
                current_position = Position.IDLE

            case Position.HASH:
                if char == "#":
                    current_position = Position.SLOT
                else:
                    buffer += "#"
                    reprocess()

            case Position.SLOT:
                if char == "[":
                    current_position = Position.CONDITION_KEY_START
                elif char in VALID_KEY_CHARS:
                    current_position = Position.KEY
                    key = char
                else:
                    buffer += "##"
                    reprocess()

            case Position.CONDITION_KEY_START:
                if char in WHITESPACE_CHARS:
                    pass
                if char in VALID_KEY_CHARS:
                    current_position = Position.CONDITION_KEY
                    key = char
                else:
                    print(f"expected key, found {char}")
                    reprocess()

            case Position.CONDITION_KEY_CLOSE:
                if char in WHITESPACE_CHARS:
                    pass
                if char == "]":
                    value = resolve_key(data, key)
                    current_position = Position.CONDITION_KEY_AFTER
                    condition_status = bool(value)
                else:
                    print(f"expected '[' found {char}")
                    reprocess()

            case Position.CONDITION_KEY_AFTER:
                if char == "{":
                    current_position = Position.CONDITION_BODY_START
                else:
                    print(f"expected '{{' found {char}")
                    reprocess()

            case Position.KEY:
                if char in VALID_KEY_CHARS:
                    key += char
                elif char == "{":
                    current_position = Position.COLLECTION_BODY_START
                elif char == "(":
                    current_position = Position.COLLECTION_JOIN
                    join_str = ""
                elif char == "#":
                    current_position = Position.END_HASH
                else:
                    buffer += "##" + key
                    reprocess()

            case Position.END_HASH:
                if char == "#":
                    buffer += str(resolve_key(data, key))
                    current_position = Position.IDLE
                else:
                    buffer += "##" + key + "#"
                    reprocess()

            case Position.CONDITION_KEY:
                if char in VALID_KEY_CHARS:
                    key += char
                elif char in WHITESPACE_CHARS:
                    current_position = Position.CONDITION_KEY_CLOSE
                elif char == "]":
                    value = resolve_key(data, key)
                    current_position = Position.CONDITION_KEY_AFTER
                    condition_status = bool(value)
                else:
                    print(f"expected ']' found {char}")
                    reprocess()

            case Position.CONDITION_BODY_START:
                if char == "{":
                    current_position = Position.CONDITION_BODY
                else:
                    print(f"expected '{{' found {char}")
                    reprocess()

            case Position.COLLECTION_BODY_START:
                if char == "{":
                    current_position = Position.COLLECTION_BODY
                else:
                    print(f"expected '{{' found {char}")
                    reprocess()

            case Position.CONDITION_BODY:
                end_index = get_body_end(plate, i)
                if end_index == -1:
                    print("bad condition body: " + plate[i:])
                    reprocess()
                else:
                    if condition_status:
                        body = trim_body(plate[i:end_index])
                        buffer += process(body, data)
                    current_position = Position.CONDITION_BODY_AFTER
                    i = end_index + 1  # Skip closing body brackets

            case Position.CONDITION_BODY_AFTER:
                if char == "{":
                    current_position = Position.CONDITION_FALLBACK_START
                else:
                    reprocess()

            case Position.CONDITION_FALLBACK_START:
                if char == "{":
                    current_position = Position.CONDITION_FALLBACK
                else:
                    buffer += "{"
                    reprocess()

            case Position.CONDITION_FALLBACK:
                end_index = get_body_end(plate, i)
                if end_index == -1:
                    print("bad fallback body: " + plate[i:])
                    reprocess()
                else:
                    if not condition_status:
                        body = trim_body(plate[i:end_index])
                        buffer += process(body, data)
                    current_position = Position.CONDITION_BODY_AFTER
                    i = end_index + 1  # Skip closing body brackets

            case Position.COLLECTION_BODY:
                end_index = get_body_end(plate, i)
                if end_index == -1:
                    print("bad collection body: " + plate[i:])
                    reprocess()
                else:
                    body = trim_body(plate[i:end_index])
                    sub_process = lambda sub_data: process(body, sub_data)
                    sub_datas = resolve_key(data, key)
                    if hasattr(sub_datas, "__iter__"):
                        results = map(sub_process, sub_datas)
                        results = filter(lambda r: r, results)  # Ignore empty strings
                        buffer += join_str.join(results)
                    else:
                        print(f"expected key with type 'list' found {type(sub_datas)}")
                    join_str = "\n"  # Reset join string after use
                    current_position = Position.IDLE
                    i = end_index + 1  # Skip closing body brackets

            case Position.COLLECTION_JOIN:
                if char == ")":
                    current_position = Position.COLLECTION_JOIN_AFTER
                elif char == "\\":
                    # All characters can be escaped in a join string
                    i += 1
                    if i < len(plate):
                        escaped_char = plate[i]
                        join_str += (
                            "\n" if escaped_char == "n"
                            else "\t" if escaped_char == "t"
                            else escaped_char
                        )
                else:
                    join_str += char

            case Position.COLLECTION_JOIN_AFTER:
                if char == "{":
                    current_position = Position.COLLECTION_BODY_START
                else:
                    print(f"expected '{{' found {char}")
                    reprocess()

            case _:
                print(f"bad position: {current_position}")
                reprocess()

        i += 1

    return buffer


def main():
    parser = argparse.ArgumentParser(
        prog="kera",
        description="Fill template files with structured data",
        epilog="README can be found at https://ctwiebe23.github.io/kera",
    )
    
    parser.add_argument(
        "files",
        nargs="*",
        help="The input files, both data and plate"
    )
    
    parser.add_argument(
        "-o", "--out-dir",
        default=".",
        help="The directory in which to write all files; defaults to the current directory",
    )
    
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    files = map(Path, args.files)
    
    if not out_dir.is_dir():
        try:
            out_dir.mkdir()
        except:
            print(f"unable to create or find directory {out_dir}")
            sys.exit(RETCODE_NOCREATE_OUTDIR)

    plates = []  # All template files; tuples of text contents and filenames
    datas = []  # All data files; tuples of text contents and filenames

    for file in files:
        if not file.is_file():
            print(f"{file} is not a file")
            continue

        name = file.stem  # Output filename defaults to the filename minus the last extension

        if file.match("*.json"):
            data = file.read_text(encoding="utf-8")
            data = json.loads(data)
            datas.append((data, name))
        elif file.match("*.yaml") or file.match("*.yml"):
            data = file.read_text(encoding="utf-8")
            data = yaml.safe_load(data)
            datas.append((data, name))
        else:
            if not file.match("*.plate"):
                # File does not need the .plate suffix stripped
                name = file.name
            plate = file.read_text(encoding="utf-8")
            plates.append((plate, name))

    for plate, plate_name in plates:
        for data, data_name in datas:
            if OUT_FILE_KEY in data:
                # Override output filename
                name = data[OUT_FILE_KEY]
            else:
                name = data_name + "_" + plate_name
            result = process(plate, data)
            (out_dir / Path(name)).write_text(result)

if __name__ == "__main__":
    main()
