from typing import List
from year_2021.day_lib import load_input_file


def problem_01(depth_list: List):
    """ Some Docstring For the Linter """
    last_depth = int(depth_list[0])
    num_increases = 0
    for depth in depth_list[1:]:
        if int(depth) >= int(last_depth):  # Need to cast these to int to prevent string compare
            num_increases = num_increases + 1
        last_depth = depth
    return num_increases


def problem_02(depth_list):
    """ Some Docstring For the Linter """
    last_depth_sum: int = int(depth_list[0]) + int(depth_list[1]) + int(depth_list[2])
    num_increases = 0
    for i, depth in enumerate(depth_list[3:]):
        curr_depth_sum = last_depth_sum - int(depth_list[i]) + int(depth)
        # print(f"{i} - {curr_depth_sum} - {last_depth_sum}")
        if curr_depth_sum > last_depth_sum:
            num_increases = num_increases + 1
        last_depth_sum = curr_depth_sum
    return num_increases


def main():
    """ Main program """
    print(f"Day 01 - Problem 01: {problem_01(load_input_file('./year_2021/input/day_01_input.txt'))}")
    print(f"Day 01 - Problem 02: {problem_02(load_input_file('./year_2021/input/day_01_input.txt'))}")

    return 0


if __name__ == "__main__":
    main()
