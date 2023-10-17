"""
Day 07 - 2020. https://adventofcode.com/2020/day/7#part2
"""


LUGGAGE = dict[str, dict[str, int]]


def number_of_bags_inside(luggage: LUGGAGE, name_bag: str) -> int:
    if name_bag not in luggage:
        return 0
    bags_inside = 0
    for color_bag, quantity in luggage[name_bag].items():
        bags_inside += quantity + quantity * number_of_bags_inside(luggage, color_bag)
    return bags_inside


def main(name_file: str) -> int:
    """
    Main function.
    """
    luggage: LUGGAGE = {}
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if not line.strip().endswith("no other bags."):
                container, contained = line.strip().split("contain")
                container = "_".join(container.strip().split(" ")[:2])
                luggage[container] = {}
                for bag in contained.split(","):
                    number, tonality, color, _ = bag.lstrip().split(" ")
                    luggage[container][f"{tonality}_{color}"] = int(number)
    return number_of_bags_inside(luggage, "shiny_gold")


if __name__ == "__main__":
    test_solution = main("day_07_2020_first_part_test_input.txt")
    assert test_solution == 32
    test_solution = main("day_07_2020_second_part_test_input.txt")
    assert test_solution == 126
    print(
        f'The solution to the second part is {main("day_07_2020_first_part_input.txt")}'
    )
