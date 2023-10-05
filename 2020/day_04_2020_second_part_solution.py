"""
Day 04 - 2020. https://adventofcode.com/2020/day/4#part2
"""

from functools import partial
from typing import Callable


def validate_year(min_year: int, max_year: int, value: str) -> bool:
    try:
        year = int(value)
        return min_year <= year <= max_year
    except ValueError:
        return False


def validate_hgt(value: str) -> bool:
    try:
        height = int(value[:-2])
        if value.endswith("cm"):
            return 150 <= height <= 193
        elif value.endswith("in"):
            return 59 <= height <= 76
    except ValueError:
        return False
    return False


def validate_hcl(value: str) -> bool:
    PERMITTED = "0123456789abcdef"
    return (
        len(value) == 7
        and value[0] == "#"
        and all(code in PERMITTED for code in value[1:])
    )


def validate_ecl(value: str) -> bool:
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_pid(value: str) -> bool:
    return len(value) == 9 and all(digit in "0123456789" for digit in value)


VALIDATE: dict[str, Callable[[str], bool]] = {
    "byr": partial(validate_year, 1920, 2002),
    "iyr": partial(validate_year, 2010, 2020),
    "eyr": partial(validate_year, 2020, 2030),
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid,
}


def valid_passport(passport: dict[str, str]) -> bool:
    return (
        len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)
    ) and all(
        VALIDATE.get(field, lambda x: True)(value) for field, value in passport.items()
    )


def main(name_file: str) -> int:
    """
    Main function.
    """
    valid_passports = 0
    passport: dict[str, str] = {}
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if len(line) > 1:
                for field_value in line.strip().split():
                    field, value = field_value.split(":")
                    passport[field] = value
            else:
                if valid_passport(passport):
                    valid_passports += 1
                passport.clear()
        if valid_passport(passport):
            valid_passports += 1
    return valid_passports


if __name__ == "__main__":
    test_solution = main("day_04_2020_second_part_test_input.txt")
    print(f"The solution to the second test part is {test_solution}")
    assert test_solution == 4
    print(
        f'The solution to the second part is {main("day_04_2020_first_part_input.txt")}'
    )
