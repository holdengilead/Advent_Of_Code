"""
Day 08 - 2020. https://adventofcode.com/2020/day/8#part2
"""


def make_run(operations):
    to_execute = 0
    accumulator = 0
    visited = set()
    while to_execute < len(operations):
        if to_execute in visited:
            return 0
        operation, value = operations[to_execute]
        visited.add(to_execute)
        if operation == "acc":
            accumulator += value
        if operation == "jmp":
            to_execute += value
        else:
            to_execute += 1
    return accumulator


def main(name_file: str) -> int:
    """
    Main function.
    """
    operations = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            operation, value = line.strip().split(" ")
            operations.append([operation, int(value)])

    for idx, op in enumerate(operations):
        if op[0] in ("jmp", "nop"):
            prev = op[0]
            operations[idx][0] = "jmp" if op[0] == "nop" else "nop"
            if accumulator := make_run(operations):
                return accumulator
            operations[idx][0] = prev


if __name__ == "__main__":
    test_solution = main("2020/day_08_2020_first_part_test_input.txt")
    assert test_solution == 8
    print(
        f'The solution to the second part is {main("2020/day_08_2020_first_part_input.txt")}'
    )
