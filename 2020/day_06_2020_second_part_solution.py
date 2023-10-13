"""
Day 06 - 2020. https://adventofcode.com/2020/day/6#part2
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    counts = 0
    with open(name_file, encoding="utf-8") as file:
        questions = []
        for line in file:
            if line.strip():
                questions.append(set(line.strip()))
            else:
                counts += len(set.intersection(*questions))
                questions.clear()
        counts += len(set.intersection(*questions))
    return counts


if __name__ == "__main__":
    test_solution = main("day_06_2020_first_part_test_input.txt")
    print(f"The solution to the second test part is {test_solution}")
    assert test_solution == 6
    print(
        f'The solution to the second part is {main("day_06_2020_first_part_input.txt")}'
    )
