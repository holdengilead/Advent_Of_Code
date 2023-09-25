"""
Day 23. https://adventofcode.com/2022/day/23
"""


from collections import defaultdict
from pprint import pprint

DIRECTIONS = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
]


def main(name_file: str) -> int:
    """
    Main function.
    """
    elves = set()
    with open(name_file, encoding="utf-8") as file:
        for x, line in enumerate(file):
            for y, pos in enumerate(line):
                if pos == "#":
                    elves.add((x, y))
    direction = 0
    for _ in range(10):
        movements = defaultdict(list)
        for elf in elves:
            if any(
                (elf[0] + x, elf[1] + y) in elves and (x != 0 or y != 0)
                for x in range(-1, 2)
                for y in range(-1, 2)
            ):  # The elf has a neighbor
                for i in range(4):
                    check = DIRECTIONS[(direction + i) % 4]
                    if all(
                        (elf[0] + move[0], elf[1] + move[1]) not in elves
                        for move in check
                    ):
                        movements[(elf[0] + check[1][0], elf[1] + check[1][1])].append(
                            elf
                        )
                        break
        for dest, pos_elv in movements.items():
            if len(pos_elv) == 1:
                elves.remove(pos_elv[0])
                elves.add(dest)
        direction = (direction + 1) % 4

    x_coords = [elf[0] for elf in elves]
    y_coords = [elf[1] for elf in elves]
    return (max(x_coords) - min(x_coords) + 1) * (
        max(y_coords) - min(y_coords) + 1
    ) - len(elves)


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_23_input_test.txt")}')
    print(f'The solution to the first part is {main("day_23_input.txt")}')
