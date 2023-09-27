"""
Day 02 - 2020. https://adventofcode.com/2020/day/2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    valid_passwords = 0
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            appearances_limit, letter, password = line.split()
            min_appearances, max_appearances = map(int, appearances_limit.split("-"))
            letter = letter[0]
            if min_appearances <= password.count(letter) <= max_appearances:
                valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    sol_test = main("day_02_2020_first_part_test_input.txt")
    print(f"The solution to the first test part is {sol_test}")
    assert sol_test == 2
    print(
        f'The solution to the first part is {main("day_02_2020_first_part_input.txt")}'
    )
