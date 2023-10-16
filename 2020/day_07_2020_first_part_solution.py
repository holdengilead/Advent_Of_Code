"""
Day 07 - 2020. https://adventofcode.com/2020/day/7
"""


from collections import defaultdict


def main(name_file: str) -> int:
    """
    Main function.
    """
    is_contained_in = defaultdict(list)
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if not line.strip().endswith("no other bags."):
                container, contained = line.strip().split("contain")
                container = "_".join(container.strip().split(" ")[:2])
                for bag in contained.split(","):
                    bag_key = "_".join(bag.lstrip().split(" ")[1:3])
                    is_contained_in[bag_key].append(container)
    bags = set()
    to_process = set(is_contained_in["shiny_gold"])
    while to_process:
        bag = to_process.pop()
        bags.add(bag)
        for bag_container in is_contained_in[bag]:
            if bag_container not in bags:
                to_process.add(bag_container)

    return len(bags)


if __name__ == "__main__":
    test_solution = main("day_07_2020_first_part_test_input.txt")
    print(f"The solution to the first test part is {test_solution}")
    assert test_solution == 4
    print(
        f'The solution to the first part is {main("day_07_2020_first_part_input.txt")}'
    )
