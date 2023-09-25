import sys


def get_grid_start_end():
    with open("day_12_input.txt", encoding="utf-8") as file:
        grid = [list(line.strip()) for line in file]
        start = None
        end = None
        for num_row, row in enumerate(grid):
            if not start and "S" in row:
                start = [num_row, row.index("S")]
            if not end and "E" in row:
                end = [num_row, row.index("E")]
            if start and end:
                break
    return grid, start, end


MOVEMENTS = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def one_step(letter_a, letter_b) -> bool:
    if letter_a == "S":
        if letter_b == "a":
            return True
        return False
    if letter_b == "E":
        if letter_a == "z":
            return True
        return False
    return (ord(letter_b.lower()) - ord(letter_a.lower())) <= 1


def main():
    grid, start, end = get_grid_start_end()
    ROWS = len(grid)
    COLS = len(grid[0])
    i = 0
    space = {tuple(start)}
    visited = set()
    while True:
        new_space = set()
        while space:
            posb = space.pop()
            visited.add(posb)
            if posb[0] == end[0] and posb[1] == end[1]:
                print(f"Minimum number of steps: {i}")
                sys.exit()
            for mov in MOVEMENTS:
                new_dest = [posb[0] + mov[0], posb[1] + mov[1]]
                if (
                    0 <= new_dest[0] < ROWS
                    and 0 <= new_dest[1] < COLS
                    and tuple(new_dest) not in visited
                    and one_step(
                        grid[posb[0]][posb[1]],
                        grid[new_dest[0]][new_dest[1]],
                    )
                ):
                    new_space.add(tuple(new_dest))
        i += 1
        space = new_space


if __name__ == "__main__":
    main()
