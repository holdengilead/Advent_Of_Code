"""
Day 09 - 2020. https://adventofcode.com/2020/day/9#part2
"""


def exists_sum(summation: int, numbers: list[int]) -> bool:
    for index, number in enumerate(numbers):
        if summation - number in numbers and numbers.index(summation - number) != index:
            return True
    return False


def find_invalid(numbers: list[int], preamble: int) -> int:
    index = preamble
    while index < len(numbers):
        if not exists_sum(numbers[index], numbers[index - preamble : index]):
            return numbers[index]
        index += 1


def main(name_file: str, preamble: int) -> int:
    """
    Main function.
    """
    numbers = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line.strip()))

    invalid_number = find_invalid(numbers, preamble)

    left, right, accum = 0, 0, 0
    while left < len(numbers):
        if right - left > 1 and accum == invalid_number:
            return min(numbers[left:right]) + max(numbers[left:right])
        elif accum < invalid_number:
            accum += numbers[right]
            right += 1
        else:
            accum -= numbers[left]
            left += 1


if __name__ == "__main__":
    test_solution = main("2020/day_09_2020_first_part_test_input.txt", 5)
    assert test_solution == 62
    print(
        f'The solution to the second part is {main("2020/day_09_2020_first_part_input.txt",25)}'
    )
