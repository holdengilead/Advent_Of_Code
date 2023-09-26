"""
Day 01 - 2020. https://adventofcode.com/2020/day/1#part2
"""
from itertools import combinations


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        numbers = {int(number) for number in file}
    for truple in combinations(numbers, 3):
        if sum(truple) == 2020:
            return truple[0] * truple[1] * truple[2]


if __name__ == "__main__":
    sol_test = main("day_01_2020_first_part_test_input.txt")
    print(
        f'The solution to the second test part is {main("day_01_2020_first_part_test_input.txt")}'
    )
    assert sol_test == 241861950
    print(
        f'The solution to the second part is {main("day_01_2020_first_part_input.txt")}'
    )
