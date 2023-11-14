"""
Day 11 - 2020. https://adventofcode.com/2020/day/11#part2
"""


def generate_adj(position) -> set[tuple[int, int]]:
    return {
        (position[0] + i, position[1] + j)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (i, j) != (0, 0)
    }


def rule_visible_occupied_seats(
    seat, free_seats, occupied_seats, limit, max_rows, max_cols
):
    occupied_visible = 0
    for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        pos_i, pos_j = seat[0] + i, seat[1] + j
        while 0 <= pos_i < max_rows and 0 <= pos_j < max_cols:
            if (pos_i, pos_j) in occupied_seats:
                occupied_visible += 1
                if occupied_visible > limit:
                    if limit == 0:
                        return False
                    return True
                break
            if (pos_i, pos_j) in free_seats:
                break
            pos_i += i
            pos_j += j
    if limit == 0:
        return True
    return False


def main(name_file: str) -> int:
    """
    Main function.
    """
    free_seats = set()
    occupied_seats = set()
    max_rows = 0
    max_cols = 0
    with open(name_file, encoding="utf-8") as file:
        for num_row, row in enumerate(file):
            max_rows += 1
            max_cols = len(row)
            for num_colum, column in enumerate(row):
                if column == "L":
                    free_seats.add((num_row, num_colum))
    while True:
        to_occupy = set()
        to_free = set()
        for seat in free_seats:
            if rule_visible_occupied_seats(
                seat, free_seats, occupied_seats, 0, max_rows, max_cols
            ):
                to_occupy.add(seat)
        for seat in occupied_seats:
            if rule_visible_occupied_seats(
                seat, free_seats, occupied_seats, 4, max_rows, max_cols
            ):
                to_free.add(seat)
        if len(to_occupy) + len(to_free) == 0:
            return len(occupied_seats)
        free_seats -= to_occupy
        free_seats |= to_free
        occupied_seats -= to_free
        occupied_seats |= to_occupy


if __name__ == "__main__":
    test_solution = main("2020/day_11_2020_first_part_test_input.txt")
    assert test_solution == 26
    print(
        f'The solution to the second part is {main("2020/day_11_2020_first_part_input.txt")}'
    )
