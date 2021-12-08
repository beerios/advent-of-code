from pathlib import Path
from typing import List


def load_input_file(file_name: str):
    in_file: Path = Path(file_name)
    if not in_file.exists():
        print(f"{file_name} does not exist or cannot be found")
        exit(-1)
    if not in_file.is_file():
        print(f"{file_name} is not a file")
        exit(-1)
    return in_file.read_text().splitlines()
