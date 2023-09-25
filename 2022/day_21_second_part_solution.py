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

    jntz = get_value(monkeys, "jntz")
    inc = 10000000000  # It came from the difference at humn = 0.
    i = 0
    while True:
        while True:
            monkeys["humn"] = [i]
            new_dif = get_value(monkeys, "prrg") - jntz
            if new_dif == 0:
                return i
            elif new_dif < 0:
                i -= inc
                inc = inc // 10
                break
            i += inc


if __name__ == "__main__":
    print(f'The solution to the second part is {main("day_21_input.txt")}')
