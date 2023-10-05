"""
Day 04 - 2020. https://adventofcode.com/2020/day/4
"""


def valid_passport(passport: set[str]) -> bool:
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)


def main(name_file: str) -> int:
    """
    Main function.
    """
    valid_passports = 0
    passport = set()
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if len(line) > 1:
                passport.update(field.split(":")[0] for field in line.strip().split())
            else:
                if valid_passport(passport):
                    valid_passports += 1
                passport = set()
        if valid_passport(passport):
            valid_passports += 1
    return valid_passports


if __name__ == "__main__":
    test_solution = main("day_04_2020_first_part_test_input.txt")
    print(f"The solution to the first test part is {test_solution}")
    assert test_solution == 2
    print(
        f'The solution to the first part is {main("day_04_2020_first_part_input.txt")}'
    )
