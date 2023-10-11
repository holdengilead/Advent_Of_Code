"""
Day 05 - 2020. https://adventofcode.com/2020/day/5#part2
"""


from collections import defaultdict


def main(name_file: str) -> int:
    """
    Main function.
    """
    plane = defaultdict(list)
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            boarding_pass = line.strip().translate({70: 48, 66: 49, 76: 48, 82: 49})
            row, col = boarding_pass[:7], boarding_pass[7:]
            plane[int(row, 2)].append(int(col, 2))

    rows = sorted(plane.keys())[1:-1]
    cols = set(range(8))
    for row in rows:
        if len(plane[row]) != 8:
            col = cols - set(plane[row])
            return row * 8 + col.pop()


if __name__ == "__main__":
    print(
        f'The solution to the second part is {main("day_05_2020_first_part_input.txt")}'
    )
