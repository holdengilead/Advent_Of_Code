DIRECTION = {"R": (0, 1), "U": (1, 0), "L": (0, -1), "D": (-1, 0)}

with open("day_09_input.txt", encoding="utf-8") as movements:
    positions = {i: [0, 0] for i in range(10)}
    places = set()
    places.add((0, 0))
    for movement in movements:
        direction, steps = movement.strip().split(" ")
        for _ in range(int(steps)):
            positions[0][0] += DIRECTION[direction][0]
            positions[0][1] += DIRECTION[direction][1]
            for i in range(1, 10):
                if 2 in (
                    abs(positions[i - 1][0] - positions[i][0]),
                    abs(positions[i - 1][1] - positions[i][1]),
                ):
                    if positions[i - 1][0] != positions[i][0]:
                        if positions[i - 1][0] > positions[i][0]:
                            positions[i][0] += 1
                        else:
                            positions[i][0] -= 1
                    if positions[i - 1][1] != positions[i][1]:
                        if positions[i - 1][1] > positions[i][1]:
                            positions[i][1] += 1
                        else:
                            positions[i][1] -= 1
            places.add(tuple(positions[9]))
    print(f"Number of positions visited: {len(places)} ")
