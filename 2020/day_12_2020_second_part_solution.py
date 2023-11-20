"""
Day 12 - 2020. https://adventofcode.com/2020/day/12#part2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    no_so_ship = 0
    es_we_ship = 0
    no_so_wayp = -1
    es_we_wayp = 10

    with open(name_file, encoding="utf-8") as file:
        for instruction in file:
            code, *value = instruction.strip()
            value = int("".join(value))
            if code == "N":
                no_so_wayp -= value
            elif code == "S":
                no_so_wayp += value
            elif code == "W":
                es_we_wayp -= value
            elif code == "E":
                es_we_wayp += value
            elif code == "F":
                no_so_ship += value * no_so_wayp
                es_we_ship += value * es_we_wayp
            else:
                value //= 90
                for _ in range(value):
                    if code == "R":
                        no_so_wayp *= -1
                    else:
                        es_we_wayp *= -1
                    no_so_wayp, es_we_wayp = es_we_wayp, no_so_wayp
    return abs(no_so_ship) + abs(es_we_ship)


if __name__ == "__main__":
    test_solution = main("2020/day_12_2020_first_part_test_input.txt")
    assert test_solution == 286
    print(
        f'The solution to the second part is {main("2020/day_12_2020_first_part_input.txt")}'
    )
