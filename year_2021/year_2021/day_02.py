from typing import List
from year_2021.day_lib import load_input_file


def problem_01(command_list: List):
    # print(f"{command_list}")
    depth: int = 0
    distance: int = 0
    for command in command_list:
        command_tuple = command.split()
        if command_tuple[0] == 'up':
            depth = depth - int(command_tuple[1])
            if depth < 0:
                depth = 0
        elif command_tuple[0] == 'down':
            depth = depth + int(command_tuple[1])
        elif command_tuple[0] == 'forward':
            distance = distance + int(command_tuple[1])
        else:
            print(f"Unrecognized Command: {command}")

    return depth * distance


def problem_02(command_list: List):
    aim: int = 0
    distance: int = 0
    depth: int = 0
    for command in command_list:
        command_tuple = command.split()
        if command_tuple[0] == 'up':
            aim = aim - int(command_tuple[1])
            if aim < 0:
                aim = 0
        elif command_tuple[0] == 'down':
            aim = aim + int(command_tuple[1])
        elif command_tuple[0] == 'forward':
            depth = depth + (aim * int(command_tuple[1]))
            distance = distance + int(command_tuple[1])
        else:
            print(f"Unrecognized Command: {command}")

    return depth * distance


def main():
    """ Main program """
    print(f"Day 02 - Problem 01: {problem_01(load_input_file('./year_2021/input/day_02_input.txt'))}")
    print(f"Day 02 - Problem 02: {problem_02(load_input_file('./year_2021/input/day_02_input.txt'))}")

    return 0


if __name__ == "__main__":
    main()
