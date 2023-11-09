"""
Day 09 - 2020. https://adventofcode.com/2020/day/9
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
    one_jolt_diff = 0
    three_jolt_diif = 1  # For the built-in
    for i in range(1, len(jolts)):
        if jolts[i] - jolts[i - 1] == 1:
            one_jolt_diff += 1
        else:
            three_jolt_diif += 1
    return one_jolt_diff * three_jolt_diif


if __name__ == "__main__":
    test_solution = main("2020/day_10_2020_first_part_test_input.txt")
    assert test_solution == 35
    test_solution = main("2020/day_10_2020_first_part_test_input_2.txt")
    assert test_solution == 220
    print(
        f'The solution to the first part is {main("2020/day_10_2020_first_part_input.txt")}'
    )
