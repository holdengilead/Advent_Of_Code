grid = []
with open("day_25.txt") as f:
    while line := f.readline().strip():
        grid.append(list(line))

dim_x = len(grid)
dim_y = len(grid[0])
is_static = False
steps = 0
while not is_static:
    is_static = True
    steps += 1
    new_grid = [["." for _ in range(dim_y)] for __ in range(dim_x)]
    for i in range(dim_x):
        for j in range(dim_y):
            if grid[i][j] == ">":
                if grid[i][(j + 1) % dim_y] == ".":
                    new_grid[i][(j + 1) % dim_y] = ">"
                    is_static = False
                else:
                    new_grid[i][j] = ">"
            elif grid[i][j] == "v":
                if (
                    grid[(i + 1) % dim_x][j] == "."
                    and grid[(i + 1) % dim_x][(j - 1) % dim_y] != ">"
                ) or (
                    grid[(i + 1) % dim_x][j] == ">"
                    and grid[(i + 1) % dim_x][(j + 1) % dim_y] == "."
                ):
                    new_grid[(i + 1) % dim_x][j] = "v"
                    is_static = False
                else:
                    new_grid[i][j] = "v"

    grid = new_grid

# for elem in grid:
#     print("".join(elem))

print(f"The sea cucumbers stop moving after {steps} steps.")
