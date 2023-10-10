"""
Day 05 - 2020. https://adventofcode.com/2020/day/5
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    highest_id = 0
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            boarding_pass = line.strip().translate({70: 48, 66: 49, 76: 48, 82: 49})
            row, col = boarding_pass[:7], boarding_pass[7:]
            boarding_pass_id = int(row, 2) * 8 + int(col, 2)
            highest_id = max(highest_id, boarding_pass_id)
    return highest_id


if __name__ == "__main__":
    test_solution = main("day_05_2020_first_part_test_input.txt")
    print(f"The solution to the first test part is {test_solution}")
    assert test_solution == 820
    print(
        f'The solution to the first part is {main("day_05_2020_first_part_input.txt")}'
    )
