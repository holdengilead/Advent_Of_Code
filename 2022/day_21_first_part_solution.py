"""
Day 21. https://adventofcode.com/2022/day/21
"""
from operator import add, floordiv, mul, sub

FUNCTIONS = {"+": add, "-": sub, "*": mul, "/": floordiv}


def get_value(monkeys: dict[str, list[str]], name: str) -> int:
    value = monkeys[name]
    if len(value) == 1:
        return int(value[0])
    return FUNCTIONS[value[1]](
        get_value(monkeys, value[0]), get_value(monkeys, value[2])
    )


def main(name_file: str) -> int:
    """
    Main function.
    """
    monkeys = {}
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            monkey, *value = line.replace(":", "").split()
            monkeys[monkey] = value

    return get_value(monkeys, "root")


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_21_input_test.txt")}')
    print(f'The solution to the first part is {main("day_21_input.txt")}')
