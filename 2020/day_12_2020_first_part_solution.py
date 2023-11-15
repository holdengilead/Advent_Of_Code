"""
Day 12 - 2020. https://adventofcode.com/2020/day/12
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    CARDINAL = "ESWN"
    direction = 0
    directions = {"N": 0, "S": 0, "W": 0, "E": 0}
    with open(name_file, encoding="utf-8") as file:
        for instruction in file:
            code, *value = instruction.strip()
            value = int("".join(value))
            if code in "NSWE":
                directions[code] += value
            elif code == "F":
                directions[CARDINAL[direction]] += value
            else:
                value //= 90
                if code == "L":
                    direction = (direction - value) % 4
                else:
                    direction = (direction + value) % 4

    return abs(directions["S"] - directions["N"]) + abs(
        directions["E"] - directions["W"]
    )


if __name__ == "__main__":
    test_solution = main("2020/day_12_2020_first_part_test_input.txt")
    assert test_solution == 25
    print(
        f'The solution to the first part is {main("2020/day_12_2020_first_part_input.txt")}'
    )
