# hydro_lines = dict()

# with open("day_5.txt", "r", encoding="utf-8") as vents:
#     for line in vents:
#         start, end = line.strip().split(" -> ")
#         x1, y1 = map(int, start.split(","))
#         x2, y2 = map(int, end.split(","))
#         if x1 == x2:
#             for i in range(min(y1, y2), max(y1, y2) + 1):
#                 hydro_lines[(x1, i)] = hydro_lines.get((x1, i), 0) + 1
#         elif y1 == y2:
#             for i in range(min(x1, x2), max(x1, x2) + 1):
#                 hydro_lines[(i, y1)] = hydro_lines.get((i, y1), 0) + 1

# print(len([value for value in hydro_lines.values() if value > 1]))


hydro_lines = dict()

with open("day_5.txt", "r", encoding="utf-8") as vents:
    for line in vents:
        start, end = line.strip().split(" -> ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                hydro_lines[(x1, i)] = hydro_lines.get((x1, i), 0) + 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                hydro_lines[(i, y1)] = hydro_lines.get((i, y1), 0) + 1
        elif abs(x2 - x1) == abs(y2 - y1):
            sign_x = 1 if x2 > x1 else -1
            sign_y = 1 if y2 > y1 else -1
            for i in range(abs(x2 - x1) + 1):
                hydro_lines[(x1 + i * sign_x, y1 + i * sign_y)] = (
                    hydro_lines.get((x1 + i * sign_x, y1 + i * sign_y), 0) + 1
                )

print(len([value for value in hydro_lines.values() if value > 1]))
