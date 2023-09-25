# import sys


# class Board:
#     def __init__(self, board) -> None:
#         self.board = board

#     def check_number(self, number):
#         for row in self.board:
#             try:
#                 pos = row.index(number)
#             except ValueError:
#                 pass
#             else:
#                 row[pos] = "X"
#                 if (
#                     "".join(row) == "XXXXX"
#                     or "".join([row[pos] for row in self.board]) == "XXXXX"
#                 ):
#                     sum_unmarked = 0
#                     for row_x in self.board:
#                         for n_x in row_x:
#                             try:
#                                 sum_unmarked += int(n_x)
#                             except ValueError:
#                                 pass
#                     print(int(number) * sum_unmarked)
#                     sys.exit()

#     def __str__(self) -> str:
#         return "\n" + "\n".join([" ".join(row) for row in self.board]) + "\n"


# class Bingo:
#     def __init__(self) -> None:
#         self.boards = []

#     def add_board(self, board):
#         self.boards.append(board)

#     def check_number(self, number):
#         for board in self.boards:
#             board.check_number(number)


# with open("day_4.txt", "r", encoding="utf-8") as data:
#     draw = data.readline().strip().split(",")
#     bingo = Bingo()
#     while True:
#         line = data.readline()
#         if not line:
#             break
#         bingo.add_board(Board([data.readline().strip().split() for _ in range(5)]))
#     for d in draw:
#         bingo.check_number(d)


class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.has_won = False

    def check_number(self, number):
        if self.has_won:
            return
        for row in self.board:
            try:
                pos = row.index(number)
            except ValueError:
                pass
            else:
                row[pos] = "X"
                if (
                    "".join(row) == "XXXXX"
                    or "".join([row[pos] for row in self.board]) == "XXXXX"
                ):
                    self.has_won = True
                    sum_unmarked = 0
                    for row_x in self.board:
                        for n_x in row_x:
                            try:
                                sum_unmarked += int(n_x)
                            except ValueError:
                                pass
                    print(int(number) * sum_unmarked)

    def __str__(self) -> str:
        return "\n" + "\n".join([" ".join(row) for row in self.board]) + "\n"


class Bingo:
    def __init__(self) -> None:
        self.boards = []

    def add_board(self, board):
        self.boards.append(board)

    def check_number(self, number):
        for board in self.boards:
            board.check_number(number)


with open("day_4.txt", "r", encoding="utf-8") as data:
    draw = data.readline().strip().split(",")
    bingo = Bingo()
    while True:
        line = data.readline()
        if not line:
            break
        bingo.add_board(Board([data.readline().strip().split() for _ in range(5)]))
    for d in draw:
        bingo.check_number(d)
