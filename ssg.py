"""
Simple SSG for the UNL OS2G website.
"""
from enum import Enum
from pathlib import Path
import shutil
import sys

class ErrorCode(Enum):
    NO_LAYOUT = 1
    NO_SRC = 2
    OUTPUT_DIR_IS_FILE = 3

if __name__ == "__main__":
    layout_path = Path("./layout.html")
    if not layout_path.is_file():
        print("ERROR : layout.html is not a file")
        sys.exit(ErrorCode.NO_LAYOUT)

    src_dir_path = Path("./src")
    if not src_dir_path.is_dir():
        print("ERROR : src is not a directory")
        sys.exit(ErrorCode.NO_SRC)

    output_dir_path = Path("./www")
    if output_dir_path.is_file():
        print("ERROR : www is a file, not a directory")
        sys.exit(ErrorCode.OUTPUT_DIR_IS_FILE)
    if not output_dir_path.is_dir():
        output_dir_path.mkdir()

    layout = layout_path.read_text(encoding="utf-8")

    def copy_dir_and_process_html(dir_path, dest_dir_path):
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
                else:
                    # shutil does *really* fast copy operations
                    shutil.copy(f"{path}", f"{dest_path}")

    copy_dir_and_process_html(src_dir_path, output_dir_path)
    sys.exit(0)
