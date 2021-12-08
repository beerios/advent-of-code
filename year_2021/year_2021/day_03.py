from typing import List
from year_2021.day_lib import load_input_file


def sum_binary_columns(binary_diagnostics: List[str]) -> List[int]:
    sums: List = []

    # sum each column and store the result
    for binary in binary_diagnostics:
        for i, c in enumerate(binary):
            if len(sums) < (i + 1):
                sums.append(0)  # initialize on the first loop
            sums[i] += int(c)
    # print(f"sums: {sums}")
    return sums


def problem_01(binary_diagnostics: List) -> int:

    sums: List[int] = sum_binary_columns(binary_diagnostics)

    gamma: str = ''
    epsilon: str = ''

    # If the sum is greater than half the number of entries, then there are more 1s than 0s in the column
    for sum in sums:
        if sum > len(binary_diagnostics)/2:
            gamma += '1'
            epsilon += '0'  # Could do this with clever binary math later (0xff), but this is easy
        else:
            gamma += '0'
            epsilon += '1'

    # print(f"gamma: {gamma}\nepsilon: {epsilon}")
    # convert the binary strings to integers
    n_gamma: int = int(gamma, 2)
    n_epsilon: int = int(epsilon, 2)

    return n_gamma * n_epsilon


def filter_diagnostics(binary_diagnostics: List[str], digit, pos) -> List[str]:
    return_val: List[str] = []
    for binary in binary_diagnostics:
        if (binary[pos] == str(digit)):
            return_val.append(binary)
    return return_val


def find_by_most_common(binary_diagnostics: List[str], pos: int):

    if len(binary_diagnostics) == 1:
        return binary_diagnostics

    # This shouldn't happen, unless there are duplicate numbers in binary_diagnostics
    if len(binary_diagnostics) < 1:
        print("ERROR: Binary Diagnostics Input is Empty")
        exit(-1)

    # This shouldn't happen, unless there are duplicate numbers in binary_diagnostics
    if pos > (len(binary_diagnostics[0]) - 1):
        print("ERROR: Binary Diagnostics Position Out of Bounds")
        exit(-1)

    most_common_digit = 0
    sums: List[int] = sum_binary_columns(binary_diagnostics)
    if sums[pos] >= len(binary_diagnostics)/2:
        most_common_digit = 1
    # print(f"Most Common Digit at {pos} is {most_common_digit}")

    return find_by_most_common(filter_diagnostics(binary_diagnostics, most_common_digit, pos), pos+1)


# Gross duplication of code 
def find_by_least_common(binary_diagnostics: List[str], pos: int):

    if len(binary_diagnostics) == 1:
        return binary_diagnostics

    # This shouldn't happen, unless there are duplicate numbers in binary_diagnostics
    if len(binary_diagnostics) < 1:
        print("ERROR: Binary Diagnostics Input is Empty")
        exit(-1)

    # This shouldn't happen, unless there are duplicate numbers in binary_diagnostics
    if pos > (len(binary_diagnostics[0]) - 1):
        print("ERROR: Binary Diagnostics Position Out of Bounds")
        exit(-1)

    least_common_digit = 0
    sums: List[int] = sum_binary_columns(binary_diagnostics)
    if sums[pos] < len(binary_diagnostics)/2:
        least_common_digit = 1
    # print(f"Least Common Digit at {pos} is {least_common_digit}")

    return find_by_least_common(filter_diagnostics(binary_diagnostics, least_common_digit, pos), pos+1)


def problem_02(binary_diagnostics: List):
    o2_generator: str = find_by_most_common(binary_diagnostics, 0)[0]
    co2_scrubber: str = find_by_least_common(binary_diagnostics, 0)[0]

    # print(f"o2 generator: {o2_generator}\nco2_scrubber: {co2_scrubber}")
    # convert the binary strings to integers
    n_o2: int = int(o2_generator, 2)
    n_co2: int = int(co2_scrubber, 2)
    # print(f"o2 generator: {n_o2}\nco2_scrubber: {n_co2}")

    return n_o2 * n_co2


def main():
    """ Main program """
    print(f"Day 03 - Problem 01: {problem_01(load_input_file('./year_2021/input/day_03_input.txt'))}")
    print(f"Day 03 - Problem 02: {problem_02(load_input_file('./year_2021/input/day_03_input.txt'))}")

    return 0


if __name__ == "__main__":
    main()
