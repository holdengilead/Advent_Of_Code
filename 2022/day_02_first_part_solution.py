"""
https://adventofcode.com/2022/day/2
"""

SCORES = {"X": 1, "Y": 2, "Z": 3}
TRANSLATION = {"X": "A", "Y": "B", "Z": "C"}
WINS = {("A", "B"), ("B", "C"), ("C", "A")}


def get_status(opponent, you):
    if opponent == you:
        return 3
    if (opponent, you) in WINS:
        return 6
    return 0


def get_score(opponent, you):
    return SCORES[you] + get_status(opponent, TRANSLATION[you])


with open("day_02_input.txt", encoding="utf-8") as file:
    print(
        sum(
            get_score(opponent, you)
            for opponent, you in (line.strip().split() for line in file)
        )
    )
