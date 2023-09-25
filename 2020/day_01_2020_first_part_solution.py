"""
Day 01 - 2020. https://adventofcode.com/2020/day/1
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        numbers = {int(number) for number in file}
    for number in numbers:
        if 2020 - number in numbers:
            return number * (2020 - number)


if __name__ == "__main__":
    sol_test = main("day_01_2020_first_part_test_input.txt")
    print(
        f'The solution to the first test part is {main("day_01_2020_first_part_test_input.txt")}'
    )
    assert sol_test == 514579
    print(
        f'The solution to the first part is {main("day_01_2020_first_part_input.txt")}'
    )
