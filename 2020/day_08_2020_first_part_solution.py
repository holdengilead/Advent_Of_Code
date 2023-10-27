"""
Day 08 - 2020. https://adventofcode.com/2020/day/8
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    operations = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            operation, value = line.strip().split(" ")
            operations.append((operation, int(value)))
    to_execute = 0
    accumulator = 0
    while True:
        if operations[to_execute] is None:
            return accumulator
        operation, value = operations[to_execute]
        operations[to_execute] = None
        if operation == "acc":
            accumulator += value
        if operation == "jmp":
            to_execute += value
        else:
            to_execute += 1


if __name__ == "__main__":
    test_solution = main("2020/day_08_2020_first_part_test_input.txt")
    assert test_solution == 5
    print(
        f'The solution to the first part is {main("2020/day_08_2020_first_part_input.txt")}'
    )
