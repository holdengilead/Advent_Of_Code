"""
Day 18. https://adventofcode.com/2022/day/18
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    area = 0
    with open(name_file, encoding="utf-8") as file:
        cubes = set(
            tuple(int(coordinate) for coordinate in line.split(",")) for line in file
        )
    for cube in cubes:
        for i in range(3):
            for inc in (1, -1):
                aux = list(cube)
                aux[i] += inc
                if tuple(aux) not in cubes:
                    area += 1
    return area


if __name__ == "__main__":
    print(f'The solution to the first part is {main("day_18_input.txt")}')
