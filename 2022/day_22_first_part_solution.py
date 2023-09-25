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
    MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self) -> None:
        self.map: list[str] = []
        self._x = 0
        self._y = None
        self.move = 0

    def add_row(self, row) -> None:
        self.map.append(row)

    def start(self) -> None:
        self._y = self.map[0].index(".")

    def execute_move(self, move: str) -> None:
        if move == "L":
            self.move = (self.move - 1) % 4
        elif move == "R":
            self.move = (self.move + 1) % 4
        else:
            move = int(move)
            while new_pos := self.can_move():
                self._x, self._y = new_pos
                move -= 1
                if not move:
                    break

    def can_move(self):
        new_x = (self._x + Jungle.MOVES[self.move][0]) % len(self.map)
        new_y = (self._y + Jungle.MOVES[self.move][1]) % len(self.map[self._x])
        if new_y >= len(self.map[new_x]) or self.map[new_x][new_y] == " ":
            new_x_mod = Jungle.MOVES[self.move][0] * -1
            new_y_mod = Jungle.MOVES[self.move][1] * -1
            new_x, new_y = self._x, self._y
            aux_new_x = (new_x + new_x_mod) % len(self.map)
            aux_new_y = (new_y + new_y_mod) % len(self.map[new_x])
            while aux_new_y < len(self.map[aux_new_x]) and (
                self.map[aux_new_x][aux_new_y]
                in {
                    ".",
                    "#",
                }
            ):
                new_x = aux_new_x
                new_y = aux_new_y
                aux_new_x = (new_x + new_x_mod) % len(self.map)
                aux_new_y = (new_y + new_y_mod) % len(self.map[new_x])
        if self.map[new_x][new_y] == ".":
            return new_x, new_y

    def get_password(self) -> int:
        return (self._x + 1) * 1000 + (self._y + 1) * 4 + self.move


def main(name_file: str) -> int:
    """
    Main function.
    """
    jungle = Jungle()
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            if not line.rstrip():
                break
            jungle.add_row(line.rstrip())
        jungle.start()
        path = JunglePath(file.readline().rstrip())
    while path:
        move = path.get_next_move()
        jungle.execute_move(move)
    return jungle.get_password()


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_22_input_test.txt")}')
    print(f'The solution to the first part is {main("day_22_input.txt")}')
