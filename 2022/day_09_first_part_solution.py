DIRECTION = {"R": (0, 1), "U": (1, 0), "L": (0, -1), "D": (-1, 0)}

with open("day_09_input.txt", encoding="utf-8") as movements:
    h_pos = [0, 0]
    t_pos = [0, 0]
    places = set((0, 0))
    for movement in movements:
        direction, steps = movement.strip().split(" ")
        for _ in range(int(steps)):
            h_pos[0] += DIRECTION[direction][0]
            h_pos[1] += DIRECTION[direction][1]
            if 2 in (abs(h_pos[0] - t_pos[0]), abs(h_pos[1] - t_pos[1])):
                if h_pos[0] != t_pos[0]:
                    if h_pos[0] > t_pos[0]:
                        t_pos[0] += 1
                    else:
                        t_pos[0] -= 1
                if h_pos[1] != t_pos[1]:
                    if h_pos[1] > t_pos[1]:
                        t_pos[1] += 1
                    else:
                        t_pos[1] -= 1
                places.add(tuple(t_pos))
    print(f"Number of positions visited: {len(places)}")
