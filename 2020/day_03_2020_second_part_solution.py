"""
Day 03 - 2020. https://adventofcode.com/2020/day/3#part2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    grid = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            grid.append(line.strip())

    MOVEMENTS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_trees = 1
    for inc_col, inc_row in MOVEMENTS:
        row, col, trees = 0, 0, 0
        COLS = len(grid[0])
        while row < len(grid) - 1:
            row += inc_row
            col = (col + inc_col) % COLS
            if grid[row][col] == "#":
                trees += 1
        total_trees *= trees
    return total_trees


if __name__ == "__main__":
    test_solution = main("day_03_2020_first_part_test_input.txt")
    print(f"The solution to the second test part is {test_solution}")
    assert test_solution == 336
    print(
        f'The solution to the second part is {main("day_03_2020_first_part_input.txt")}'
    )
