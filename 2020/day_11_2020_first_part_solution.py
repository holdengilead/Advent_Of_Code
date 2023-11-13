"""
Day 11 - 2020. https://adventofcode.com/2020/day/11
"""


def generate_adj(position) -> set[tuple[int, int]]:
    return {
        (position[0] + i, position[1] + j)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (i, j) != (0, 0)
    }


def main(name_file: str) -> int:
    """
    Main function.
    """
    free_seats = set()
    occupied_seats = set()
    with open(name_file, encoding="utf-8") as file:
        for num_row, row in enumerate(file):
            for num_colum, column in enumerate(row):
                if column == "L":
                    free_seats.add((num_row, num_colum))
    while True:
        to_occupy = set()
        to_free = set()
        for seat in free_seats:
            if len(generate_adj(seat) & occupied_seats) == 0:
                to_occupy.add(seat)
        for seat in occupied_seats:
            if len(generate_adj(seat) & occupied_seats) >= 4:
                to_free.add(seat)
        if len(to_occupy) + len(to_free) == 0:
            return len(occupied_seats)
        free_seats -= to_occupy
        free_seats |= to_free
        occupied_seats -= to_free
        occupied_seats |= to_occupy


if __name__ == "__main__":
    test_solution = main("2020/day_11_2020_first_part_test_input.txt")
    assert test_solution == 37
    print(
        f'The solution to the first part is {main("2020/day_11_2020_first_part_input.txt")}'
    )
