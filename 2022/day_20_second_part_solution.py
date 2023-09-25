"""
Day 20. https://adventofcode.com/2022/day/20
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    decription_key = 811589153
    with open(name_file, encoding="utf-8") as file:
        numbers = [int(line) * decription_key for line in file]

    modulus = len(numbers) - 1
    positions = list(range(len(numbers)))
    zero_pos = numbers.index(0)

    for iteration in range(10):
        for pos, value in enumerate(numbers):
            old_value = positions[pos]
            positions[pos] = (positions[pos] + value) % modulus
            new_value = positions[pos]
            for i in range(len(positions)):
                if new_value > old_value:
                    if i != pos and old_value < positions[i] <= new_value:
                        positions[i] -= 1
                else:
                    if i != pos and new_value <= positions[i] < old_value:
                        positions[i] += 1

    new_zero_pos = positions[zero_pos]
    res = 0
    for i in (1000, 2000, 3000):
        th_pos = (new_zero_pos + i) % len(numbers)
        res += numbers[positions.index(th_pos)]
    return res


if __name__ == "__main__":
    print(f'The solution to the second test part is {main("day_20_input_test.txt")}')
    print(f'The solution to the second part is {main("day_20_input.txt")}')
