"""
Simple SSG that generates a website using kera.
"""

from pathlib import Path
import shutil
import sys
import kera
import json

# return codes
RETCODE_OK = 0
RETCODE_NO_LAYOUT = 1
RETCODE_NO_SRC = 2
RETCODE_OUTPUT_DIR_IS_FILE = 3
RETCODE_NO_DATA = 4

if __name__ == "__main__":
    layout_path = Path("./layout.html")
    if not layout_path.is_file():
        print(f"ERROR : {layout_path} is not a file")
        sys.exit(RETCODE_NO_LAYOUT)

    src_dir_path = Path("./src")
    if not src_dir_path.is_dir():
        print(f"ERROR : {src_dir_path} is not a directory")
        sys.exit(RETCODE_NO_SRC)

    data_path = Path("./data.json")
    if not data_path.is_file():
        print(f"ERROR : {data_path} is not a file")
        sys.exit(RETCODE_NO_DATA)

    output_dir_path = Path("./www")
    if output_dir_path.is_file():
        print(f"ERROR : {output_dir_path} is a file, not a directory")
        sys.exit(RETCODE_OUTPUT_DIR_IS_FILE)
    if not output_dir_path.is_dir():
        output_dir_path.mkdir()

    layout = layout_path.read_text(encoding="utf-8")
    data = data_path.read_text(encoding="utf-8")
    data = json.loads(data)

    def copy_dir_and_process_html(dir_path: Path, dest_dir_path: Path):
        """
        Copies the contents of the directory at dir_path into the directory at
        dest_dir_path.  Inserts every HTML file it encounters into the layout
        before copying.
        """
        for path in dir_path.iterdir():
            dest_path = dest_dir_path / path.name

            if path.is_dir():
                if dest_path.is_file():
                    print(f"ERROR : naming conflict: {dest_path}")
                    sys.exit(4)
                if not dest_path.is_dir():
                    dest_path.mkdir()
                # recursively operate on the inner directory
                copy_dir_and_process_html(path, dest_path)
            else: # handling a file
                if path.match("*.html"):
                    contents = path.read_text(encoding="utf-8")
                    page = layout.replace("##CONTENTS##", contents)
                    dest_path.write_text(page)
                elif path.match("*.plate"):
                    dest_path = dest_path.with_suffix("") # remove .plate suffix
                    contents = path.read_text(encoding="utf-8")
                    generated = kera.process(contents, data)
                    if dest_path.match("*.html"):
                        generated = layout.replace("##CONTENTS##", generated)
                    dest_path.write_text(generated)
                else:
                    shutil.copy(str(path), str(dest_path))

    copy_dir_and_process_html(src_dir_path, output_dir_path)
    sys.exit(RETCODE_OK)
