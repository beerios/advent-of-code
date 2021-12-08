from pathlib import Path
from typing import List
from year_2021 import day_01, day_02, day_03


def load_input_file(file_name: str) -> List[str]:
    in_file: Path = Path(file_name)
    if not in_file.exists():
        print(f"{file_name} does not exist or cannot be found")
        raise SystemExit(-1)
    if not in_file.is_file():
        print(f"{file_name} is not a file")
        raise SystemExit(-1)
    return in_file.read_text().splitlines()


def test_day_01():
    assert day_01.problem_01(load_input_file("./tests/input/day_01_test.txt")) == 7
    assert day_01.problem_02(load_input_file("./tests/input/day_01_test.txt")) == 5


def test_day_02():
    assert day_02.problem_01(load_input_file("./tests/input/day_02_test.txt")) == 150
    assert day_02.problem_02(load_input_file("./tests/input/day_02_test.txt")) == 900


def test_day_03():
    assert day_03.problem_01(load_input_file("./tests/input/day_03_test.txt")) == 198
    assert day_03.problem_02(load_input_file("./tests/input/day_03_test.txt")) == 230
