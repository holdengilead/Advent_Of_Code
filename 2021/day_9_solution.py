# with open("day_9.txt", "r", encoding="utf-8") as points:
#     heights = dict()
#     risk_level = 0
#     for i in range(100):
#         line = list(points.readline().strip())
#         for j in range(len(line)):
#             heights[(i, j)] = int(line[j])
#     for point, height in heights.items():
#         if height < min(
#             heights.get((point[0] - 1, point[1]), height + 1),
#             heights.get((point[0], point[1] + 1), height + 1),
#             heights.get((point[0] + 1, point[1]), height + 1),
#             heights.get((point[0], point[1] - 1), height + 1),
#         ):
#             risk_level += height + 1

#     print(risk_level)


with open("day_9.txt", "r", encoding="utf-8") as points:
    heights = dict()
    low_points = []
    for i in range(100):
        line = list(points.readline().strip())
        for j in range(len(line)):
            heights[(i, j)] = int(line[j])
    for point, height in heights.items():
        if height < min(
            heights.get((point[0] - 1, point[1]), height + 1),
            heights.get((point[0], point[1] + 1), height + 1),
            heights.get((point[0] + 1, point[1]), height + 1),
            heights.get((point[0], point[1] - 1), height + 1),
        ):
            low_points.append(point)

    basins = dict()
    for point in low_points:
        # print(f"Visito el low point {point}")
        to_visit = [point]
        basins[point] = set()
        # print(f"\tEl basin : {basins[point]}")
        # print(f"\tEl to_visit : {to_visit}")
        while to_visit:
            aux = to_visit.pop()
            # print(f"\tEl to_visit : {to_visit}")
            basins[point].add(aux)
            # print(f"\tEl basin : {basins[point]}")
            for mov in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                vecino = (aux[0] + mov[0], aux[1] + mov[1])
                if (
                    vecino in heights
                    and heights[vecino] != 9
                    and vecino not in basins[point]
                ):
                    to_visit.append(vecino)
                    # print(f"\tEl to_visit : {to_visit}")
    # print(basins)
    three_largest = sorted(
        [len(basin) for low_point, basin in basins.items()], reverse=True
    )[:3]
    print(three_largest[0] * three_largest[1] * three_largest[2])
