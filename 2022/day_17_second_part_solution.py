"""
Day 17. https://adventofcode.com/2022/day/17
"""


import itertools

Point = tuple[int, int]
LATERAL = {">": lambda x: (x[0] + 1, x[1]), "<": lambda x: (x[0] - 1, x[1])}


class Piece:
    def __init__(self, highest: int) -> None:
        self.high = highest + 4
        self.points = []
        self._projection = None

    def can_move(self, points: set[Point]) -> bool:
        self._projection = tuple((point[0], point[1] - 1) for point in self.points)
        return min(
            point[1] for point in self._projection
        ) >= 1 and not points.intersection(self._projection)

    def down(self) -> None:
        self.points = self._projection

    def lateral(self, movement: str, points: set[Point]) -> None:
        projection = tuple(LATERAL[movement](point) for point in self.points)
        if (
            min(point[0] for point in projection) >= 0
            and max(point[0] for point in projection) <= 6
            and not points.intersection(projection)
        ):
            self.points = projection


class Horizontal(Piece):
    def __init__(self, highest: int) -> None:
        super().__init__(highest)
        self.points = (
            (2, self.high),
            (3, self.high),
            (4, self.high),
            (5, self.high),
        )


class Cross(Piece):
    def __init__(self, highest: int) -> None:
        super().__init__(highest)
        self.points = (
            (3, self.high),
            (3, self.high + 1),
            (3, self.high + 2),
            (2, self.high + 1),
            (4, self.high + 1),
        )


class Ele(Piece):
    def __init__(self, highest: int) -> None:
        super().__init__(highest)
        self.points = (
            (2, self.high),
            (3, self.high),
            (4, self.high),
            (4, self.high + 1),
            (4, self.high + 2),
        )


class Vertical(Piece):
    def __init__(self, highest: int) -> None:
        super().__init__(highest)
        self.points = (
            (2, self.high),
            (2, self.high + 1),
            (2, self.high + 2),
            (2, self.high + 3),
        )


class Square(Piece):
    def __init__(self, highest: int) -> None:
        super().__init__(highest)
        self.points = (
            (2, self.high),
            (3, self.high),
            (2, self.high + 1),
            (3, self.high + 1),
        )


def main(name_file: str) -> None:
    """
    Main function.
    """
    pieces = itertools.cycle((Horizontal, Cross, Ele, Vertical, Square))
    with open(name_file, encoding="utf-8") as file:
        lateral_moves = itertools.cycle(file.readline())
    points = set()
    highest = 0
    old_highest = 0
    for x in range(1, 2023):
        piece: Piece = next(pieces)(highest=highest)
        piece.lateral(next(lateral_moves), points=points)
        while piece.can_move(points):
            piece.down()
            piece.lateral(next(lateral_moves), points=points)
        points.update(piece.points)
        highest = max(highest, *(point[1] for point in piece.points))
        if x % 5 == 0:
            print(highest - old_highest)
            old_highest = highest

    return highest


if __name__ == "__main__":
    # print(f'The solution to the first part is {main("day_17_input_test.txt")}')
    print(f'The solution to the first part is {main("day_17_input.txt")}')
