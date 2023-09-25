"""
Day 18. https://adventofcode.com/2022/day/18
"""

Cube = tuple[int, int, int]


def in_space(cube: Cube, min_c: Cube, max_c: Cube) -> bool:
    return all(min_c[i] <= cube[i] <= max_c[i] for i in range(3))


def get_neighbors(cube: Cube) -> list[Cube]:
    return [
        tuple(sum(x) for x in zip(cube, d))
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    ]


def main(name_file: str) -> int:
    """
    Main function.
    """
    area = 0
    with open(name_file, encoding="utf-8") as file:
        cubes = set(
            tuple(int(coordinate) for coordinate in line.split(",")) for line in file
        )

    min_cube = tuple(min(c[i] - 1 for c in cubes) for i in range(3))
    max_cube = tuple(max(c[i] + 1 for c in cubes) for i in range(3))

    seen = set()
    to_explore = [max_cube]
    while to_explore:
        cube = to_explore.pop()
        if cube in cubes:
            area += 1
        else:
            if cube not in seen:
                seen.add(cube)
                for neig in get_neighbors(cube):
                    if in_space(neig, min_cube, max_cube):
                        to_explore.append(neig)

    return area


if __name__ == "__main__":
    print(f'The solution to the second test part is {main("day_18_input_test.txt")}')
    print(f'The solution to the second part is {main("day_18_input.txt")}')
