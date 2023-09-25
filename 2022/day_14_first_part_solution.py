def main():
    obstacles = set()
    abyss = 0
    with open("day_14_input.txt", encoding="utf-8") as file:
        while line := file.readline().strip():
            lines_rock = line.split(" -> ")
            for i in range(len(lines_rock) - 1):
                rock_1_x, rock_1_y = map(int, lines_rock[i].split(","))
                rock_2_x, rock_2_y = map(int, lines_rock[i + 1].split(","))
                abyss = max(abyss, rock_1_y, rock_2_y)
                for j in range(min(rock_1_x, rock_2_x), max(rock_1_x, rock_2_x) + 1):
                    for k in range(
                        min(rock_1_y, rock_2_y), max(rock_1_y, rock_2_y) + 1
                    ):
                        obstacles.add((j, k))
    sand = 0
    while True:
        particle = [500, 0]
        while True:
            if particle[1] > abyss:
                return sand
            if (particle[0], particle[1] + 1) not in obstacles:
                particle[1] += 1
            elif (particle[0] - 1, particle[1] + 1) not in obstacles:
                particle[0] -= 1
                particle[1] += 1
            elif (particle[0] + 1, particle[1] + 1) not in obstacles:
                particle[0] += 1
                particle[1] += 1
            else:
                sand += 1
                obstacles.add(tuple(particle))
                break


if __name__ == "__main__":
    print(main())
