"""
Day 03 - 2020. https://adventofcode.com/2020/day/3
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    trees = 0
    grid = []
    row, col = 0, 0
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            grid.append(line.strip())
    COLS = len(grid[0])
    while row < len(grid) - 1:
        row += 1
        col = (col + 3) % COLS
        if grid[row][col] == "#":
            trees += 1
    return trees


if __name__ == "__main__":
    test_solution = main("day_03_2020_first_part_test_input.txt")
    print(f"The solution to the first test part is {test_solution}")
    assert test_solution == 7
    print(
        f'The solution to the first part is {main("day_03_2020_first_part_input.txt")}'
    )
