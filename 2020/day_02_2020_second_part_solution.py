"""
Day 02 - 2020. https://adventofcode.com/2020/day/2#part2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    valid_passwords = 0
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            positions, letter, password = line.split()
            first, second = map(int, positions.split("-"))
            letter = letter[0]
            if (password[first - 1] == letter) ^ (password[second - 1] == letter):
                valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    sol_test = main("day_02_2020_first_part_test_input.txt")
    print(f"The solution to the second test part is {sol_test}")
    assert sol_test == 1
    print(
        f'The solution to the second part is {main("day_02_2020_first_part_input.txt")}'
    )
