"""
Day 14 - 2020. https://adventofcode.com/2020/day/14
"""


def main(name_file: str) -> int:
    """
    Main function.
    """
    mask = None
    memory = {}
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if line.startswith("mask"):
                _, mask = line.split("=")
                mask = mask.strip()
            else:
                address = line[4 : line.index("]")]
                _, value = line.split("=")
                value = "0" * (36 - len(bin(int(value))[2:])) + bin(int(value))[2:]
                memory[address] = int(
                    "".join(v if m == "X" else m for v, m in zip(value, mask)), 2
                )

    return sum(memory.values())


if __name__ == "__main__":
    test_solution = main("2020/day_14_2020_first_part_test_input.txt")
    assert test_solution == 165
    print(
        f'The solution to the first part is {main("2020/day_14_2020_first_part_input.txt")}'
    )
