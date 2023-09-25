"""
Day 24. https://adventofcode.com/2022/day/24
"""


from math import inf


class Storm:
    MOVES = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}

    def __init__(self, last_row: int, last_col: int, blizzards=None) -> None:
        if blizzards:
            self._blizzards = blizzards
        else:
            self._blizzards = set()
        self.last_row = last_row
        self.last_col = last_col

    def add(self, num_row: int, num_col: int, direct: str) -> None:
        self._blizzards.add((num_row, num_col, direct))

    def move(self) -> None:
        aux = set()
        for blizzard in self._blizzards:
            _x, _y, _d = blizzard
            new_x, new_y = _x + Storm.MOVES[_d][0], _y + Storm.MOVES[_d][1]
            if new_y == 0:
                new_y = self.last_col
            elif new_y == self.last_col + 1:
                new_y = 1
            elif new_x == 0:
                new_x = self.last_row
            elif new_x == self.last_row + 1:
                new_x = 1
            aux.add((new_x, new_y, _d))
        self._blizzards = aux

    def __contains__(self, pos) -> bool:
        return any((pos[0], pos[1], direct) in self._blizzards for direct in "<^v>")

    def copy(self):
        return Storm(self.last_row, self.last_col, self._blizzards.copy())

    def frozen(self):
        return frozenset(self._blizzards)


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        grid = file.read().split("\n")
    elf_pos = (0, 1)
    end = (len(grid) - 1, len(grid[-1]) - 2)
    walls = set()
    walls.add((-1, 1))  # Pongo un wall para evitar que se escape del grid.
    storm = Storm(last_row=len(grid) - 2, last_col=len(grid[-1]) - 2)
    best_short_route = inf
    for num_row, row in enumerate(grid):
        for num_col, element in enumerate(row):
            if element == "#":
                walls.add((num_row, num_col))
            elif element in "<^v>":
                storm.add(num_row, num_col, direct=element)
    space = [(elf_pos, 0, storm)]
    visited = set()
    while space:
        e_pos, minutes, storm = space.pop()
        visited.add((e_pos, storm.frozen()))
        if (
            minutes + abs(end[0] - e_pos[0]) + abs(end[1] - e_pos[1])
            >= best_short_route
        ):
            continue
        if e_pos == end:
            best_short_route = min(best_short_route, minutes)
            print(f"{best_short_route=}")
            input()
        else:
            storm.move()
            changes = 0
            for elf_move in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
                new_elf_pos_x, new_elf_pos_y = (
                    e_pos[0] + elf_move[0],
                    e_pos[1] + elf_move[1],
                )
                if (
                    (new_elf_pos_x, new_elf_pos_y) not in walls
                    and (
                        new_elf_pos_x,
                        new_elf_pos_y,
                    )
                    not in storm
                    and ((new_elf_pos_x, new_elf_pos_y), storm.frozen()) not in visited
                ):
                    space.append(
                        ((new_elf_pos_x, new_elf_pos_y), minutes + 1, storm.copy())
                    )
                    changes += 1
            if changes:
                space.sort(
                    key=lambda x: (end[0] - x[0][0]) ** 2 + (end[1] - x[0][1]) ** 2,
                    reverse=True,
                )

    return best_short_route


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_24_input_test.txt")}')
    print(
        f'The solution to the first part is {main("day_24_input.txt")}'
    )  # Stop at best_short_route = 264
