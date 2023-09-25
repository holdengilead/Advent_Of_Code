"""
Day 22. https://adventofcode.com/2022/day/22
"""


class JunglePath:
    NUMBERS = {n for n in "0123456789"}

    def __init__(self, path: str) -> None:
        self.path = path
        self._pos = 0

    def __bool__(self) -> bool:
        return self._pos < len(self.path)

    def get_next_move(self) -> None:
        move = self.path[self._pos]
        self._pos += 1
        if move in "LR":
            return move
        while self._pos < len(self.path) and self.path[self._pos] in JunglePath.NUMBERS:
            move += self.path[self._pos]
            self._pos += 1
        return move


class Jungle:
    OFFSETS = {
        50: {
            "offset_x": {1: 0, 2: 0, 3: 1, 4: 2, 5: 2, 6: 3},
            "offset_y": {1: 1, 2: 2, 3: 1, 4: 1, 5: 0, 6: 0},
        },
        4: {
            "offset_x": {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2},
            "offset_y": {1: 2, 2: 0, 3: 1, 4: 2, 5: 2, 6: 3},
        },
    }
    NEXT_CUBE = {
        4: {
            (1, 0): (6, 2, (lambda x, y, s: y - x), (lambda x, y, s: y)),
            (1, 1): (4, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (1, 2): (3, 1, (lambda x, y, s: 0), (lambda x, y, s: x)),
            (1, 3): (2, 1, (lambda x, y, s: 0), (lambda x, y, s: s - y)),
            (2, 0): (3, 0, (lambda x, y, s: x), (lambda x, y, s: 0)),
            (2, 1): (5, 3, (lambda x, y, s: s), (lambda x, y, s: s - y)),
            (2, 2): (6, 3, (lambda x, y, s: s), (lambda x, y, s: s - x)),
            (2, 3): (1, 1, (lambda x, y, s: 0), (lambda x, y, s: s - y)),
            (3, 0): (4, 0, (lambda x, y, s: x), (lambda x, y, s: 0)),
            (3, 1): (5, 0, (lambda x, y, s: s - y), (lambda x, y, s: 0)),
            (3, 2): (2, 2, (lambda x, y, s: x), (lambda x, y, s: s)),
            (3, 3): (1, 0, (lambda x, y, s: y), (lambda x, y, s: 0)),
            (4, 0): (6, 1, (lambda x, y, s: 0), (lambda x, y, s: s - x)),
            (4, 1): (5, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (4, 2): (3, 2, (lambda x, y, s: x), (lambda x, y, s: s)),
            (4, 3): (1, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
            (5, 0): (6, 0, (lambda x, y, s: x), (lambda x, y, s: 0)),
            (5, 1): (2, 3, (lambda x, y, s: s), (lambda x, y, s: s - y)),
            (5, 2): (3, 3, (lambda x, y, s: s), (lambda x, y, s: s - x)),
            (5, 3): (4, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
            (6, 0): (1, 2, (lambda x, y, s: s - x), (lambda x, y, s: s)),
            (6, 1): (2, 0, (lambda x, y, s: s - y), (lambda x, y, s: 0)),
            (6, 2): (5, 2, (lambda x, y, s: x), (lambda x, y, s: s)),
            (6, 3): (4, 2, (lambda x, y, s: s - y), (lambda x, y, s: s)),
        },
        50: {
            (1, 0): (2, 0, (lambda x, y, s: x), (lambda x, y, s: 0)),
            (1, 1): (3, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (1, 2): (5, 0, (lambda x, y, s: s - x), (lambda x, y, s: 0)),
            (1, 3): (6, 0, (lambda x, y, s: y), (lambda x, y, s: 0)),
            (2, 0): (4, 2, (lambda x, y, s: s - x), (lambda x, y, s: s)),
            (2, 1): (3, 2, (lambda x, y, s: y), (lambda x, y, s: s)),
            (2, 2): (1, 2, (lambda x, y, s: x), (lambda x, y, s: s)),
            (2, 3): (6, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
            (3, 0): (2, 3, (lambda x, y, s: s), (lambda x, y, s: x)),
            (3, 1): (4, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (3, 2): (5, 1, (lambda x, y, s: 0), (lambda x, y, s: x)),
            (3, 3): (1, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
            (4, 0): (2, 2, (lambda x, y, s: s - x), (lambda x, y, s: s)),
            (4, 1): (6, 2, (lambda x, y, s: y), (lambda x, y, s: s)),
            (4, 2): (5, 2, (lambda x, y, s: x), (lambda x, y, s: s)),
            (4, 3): (3, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
            (5, 0): (4, 0, (lambda x, y, s: x), (lambda x, y, s: 0)),
            (5, 1): (6, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (5, 2): (1, 0, (lambda x, y, s: s - x), (lambda x, y, s: 0)),
            (5, 3): (3, 0, (lambda x, y, s: y), (lambda x, y, s: 0)),
            (6, 0): (4, 3, (lambda x, y, s: s), (lambda x, y, s: x)),
            (6, 1): (2, 1, (lambda x, y, s: 0), (lambda x, y, s: y)),
            (6, 2): (1, 1, (lambda x, y, s: 0), (lambda x, y, s: x)),
            (6, 3): (5, 3, (lambda x, y, s: s), (lambda x, y, s: y)),
        },
    }
    MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, size: int) -> None:
        self._x = 0
        self._y = 0
        self.cube = 1
        self.map: dict[int, list[str]] = {}
        self.move = 0
        self.offset_x = Jungle.OFFSETS[size]["offset_x"]
        self.offset_y = Jungle.OFFSETS[size]["offset_y"]
        self.size = size
        self.next_cube = Jungle.NEXT_CUBE[size]

    def read_cubes(self, map: list[str]) -> None:
        for i in range(1, 7):
            self.map[i] = []
            for j in range(self.size):
                row = self.offset_x[i] * self.size + j
                start_col = self.offset_y[i] * self.size
                end_col = start_col + self.size
                self.map[i].append(map[row][start_col:end_col])

    def execute_move(self, move: str) -> None:
        if move == "L":
            self.move = (self.move - 1) % 4
        elif move == "R":
            self.move = (self.move + 1) % 4
        else:
            move = int(move)
            while new_pos := self.can_move():
                self.cube, self._x, self._y, self.move = new_pos
                move -= 1
                if not move:
                    break

    def can_move(self):
        new_x = self._x + Jungle.MOVES[self.move][0]
        new_y = self._y + Jungle.MOVES[self.move][1]
        new_cube = self.cube
        new_move = self.move
        if not (0 <= new_x < self.size and 0 <= new_y < self.size):
            new_cube, new_move, mod_x, mod_y = self.next_cube[(self.cube, self.move)]
            new_x = mod_x(self._x, self._y, self.size - 1)
            new_y = mod_y(self._x, self._y, self.size - 1)
        if self.map[new_cube][new_x][new_y] == ".":
            return new_cube, new_x, new_y, new_move

    def get_password(self) -> int:
        return (
            (self._x + 1 + self.offset_x[self.cube] * self.size) * 1000
            + (self._y + 1 + self.offset_y[self.cube] * self.size) * 4
            + self.move
        )


def main(name_file: str, size: int) -> int:
    """
    Main function.
    """
    aux_jungle = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if not line.rstrip():
                break
            aux_jungle.append(line.rstrip())
        path = JunglePath(file.readline().rstrip())
    jungle = Jungle(size)
    jungle.read_cubes(aux_jungle)
    while path:
        move = path.get_next_move()
        jungle.execute_move(move)
    return jungle.get_password()


if __name__ == "__main__":
    print(f'The solution to the second test part is {main("day_22_input_test.txt",4)}')
    print(f'The solution to the second part is {main("day_22_input.txt",50)}')
