BORDERS = {0, 98}
MOVEMENTS = {(-1, 0), (1, 0), (0, -1), (0, 1)}

with open("day_08_input.txt", encoding="utf-8") as file:
    grid = [line.strip() for line in file]
    max_scenic_score = 0
    for row in range(1, 98):
        for column in range(1, 98):
            value = int(grid[row][column])
            scenic_score = 1
            if value > 7:
                for mov in MOVEMENTS:
                    direc_scenic = 0
                    aux_row = row
                    aux_col = column
                    while True:
                        direc_scenic += 1
                        aux_row += mov[0]
                        aux_col += mov[1]
                        if (
                            int(grid[aux_row][aux_col]) >= value
                            or aux_row in BORDERS
                            or aux_col in BORDERS
                        ):
                            scenic_score *= direc_scenic
                            break
            max_scenic_score = max(max_scenic_score, scenic_score)

    print(f"Maximum scenic score: {max_scenic_score}")
