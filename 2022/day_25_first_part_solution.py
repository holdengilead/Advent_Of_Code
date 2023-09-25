"""
Day 25. https://adventofcode.com/2022/day/25
"""
from itertools import zip_longest

S_T_D_VALUE = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
D_T_S_VALUE = {
    -5: ("0", -1),
    -4: ("1", -1),
    -3: ("2", -1),
    -2: ("=", 0),
    -1: ("-", 0),
    0: ("0", 0),
    1: ("1", 0),
    2: ("2", 0),
    3: ("=", 1),
    4: ("-", 1),
    5: ("0", 1),
}


def sum_snafu(first: str, second: str) -> str:
    acc = 0
    snafu = ""
    for num_1, num_2 in zip_longest(first[::-1], second[::-1], fillvalue="0"):
        num_1, num_2 = S_T_D_VALUE[num_1], S_T_D_VALUE[num_2]
        res, acc = D_T_S_VALUE[acc + num_1 + num_2]
        snafu += res
    return f'{acc if acc else ""}{snafu[::-1]}'


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        accumulator = file.readline().strip()
        for line in file:
            accumulator = sum_snafu(accumulator, line.strip())
        return accumulator


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_25_input_test.txt")}')
    print(f'The solution to the first part is {main("day_25_input.txt")}')
