"""
Day 13 - 2020. https://adventofcode.com/2020/day/13
"""


from math import inf


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        earliest_departure = int(file.readline().strip())
        buses = (
            int(bus_id)
            for bus_id in file.readline().strip().split(",")
            if bus_id != "x"
        )
        min_wait = inf
        bus_min_wait = None
        for bus in buses:
            wait_time = (
                0 if earliest_departure % bus == 0 else bus - (earliest_departure % bus)
            )
            if wait_time < min_wait:
                min_wait = wait_time
                bus_min_wait = bus

        return min_wait * bus_min_wait


if __name__ == "__main__":
    test_solution = main("2020/day_13_2020_first_part_test_input.txt")
    assert test_solution == 295
    print(
        f'The solution to the first part is {main("2020/day_13_2020_first_part_input.txt")}'
    )
