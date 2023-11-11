"""
Day 09 - 2020. https://adventofcode.com/2020/day/10#part2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    jolts = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            jolts.append(int(line.strip()))
    jolts.sort()
    jolts = [0] + jolts
    arrangements = {jolts[-1]: 1}
    for elem in reversed(jolts[:-1]):
        arrangements[elem] = (
            arrangements.get(elem + 1, 0)
            + arrangements.get(elem + 2, 0)
            + arrangements.get(elem + 3, 0)
        )
    return arrangements[0]


if __name__ == "__main__":
    test_solution = main("2020/day_10_2020_first_part_test_input.txt")
    assert test_solution == 8
    test_solution = main("2020/day_10_2020_first_part_test_input_2.txt")
    assert test_solution == 19208
    print(
        f'The solution to the second part is {main("2020/day_10_2020_first_part_input.txt")}'
    )
