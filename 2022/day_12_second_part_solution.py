def get_grid_start_end():
    with open("day_12_input.txt", encoding="utf-8") as file:
        grid = [list(line.strip()) for line in file]
        start = None
        end = None
        possible_starts = set()
        for num_row, row in enumerate(grid):
            for num_col, value in enumerate(row):
                if value == "S":
                    start = [num_row, num_col]
                elif value == "E":
                    end = [num_row, num_col]
                elif value == "a":
                    possible_starts.add((num_row, num_col))
    return grid, start, end, possible_starts


MOVEMENTS = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def one_step(letter_a, letter_b) -> bool:
    if letter_b == "E":
        if letter_a == "z":
            return True
        return False
    return (ord(letter_b) - ord(letter_a)) <= 1


def get_shortest_route(grid, start, end, min_steps):
    ROWS = len(grid)
    COLS = len(grid[0])
    i = 0
    space = {tuple(start)}
    visited = set()
    while True:
        if i == min_steps:
            return min_steps
        new_space = set()
        while space:
            try:
                posb = space.pop()
            except KeyError:  # Maybe there isn't a route.
                return min_steps
            visited.add(posb)
            if posb[0] == end[0] and posb[1] == end[1]:
                return i
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


def main():
    minimum_steps = 490  # It was the answer to the first part, starting from S.
    grid, start, end, possible_starts = get_grid_start_end()
    grid[start[0]][start[1]] = "a"
    for pos in possible_starts:
        minimum_steps = get_shortest_route(grid, pos, end, minimum_steps)
    print(f"Minimum steps for all possible starts: {minimum_steps}")


if __name__ == "__main__":
    main()
