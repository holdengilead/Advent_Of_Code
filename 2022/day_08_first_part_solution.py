BORDERS = {0, 98}

with open("day_08_input.txt", encoding="utf-8") as file:
    rows = [line.strip() for line in file]
    columns = list(elem for elem in zip(*rows))
    num_visible = 0
    for row in range(99):
        for column in range(99):
            value = rows[row][column]
            if (
                {row, column} & BORDERS != set()
                or value > max(rows[row][:column])
                or value > max(rows[row][column + 1 :])
                or value > max(columns[column][:row])
                or value > max(columns[column][row + 1 :])
            ):
                num_visible += 1
    print(f"Tree visibles: {num_visible}")
