"""
https://adventofcode.com/2022/day/2
"""

VALUES = {"A": 1, "B": 2, "C": 3}
TO_WIN = {"A": "B", "B": "C", "C": "A"}
TO_LOSE = {"A": "C", "B": "A", "C": "B"}
FUNC = {
    "X": (lambda x: VALUES[TO_LOSE[x]]),
    "Y": (lambda x: 3 + VALUES[x]),
    "Z": (lambda x: 6 + VALUES[TO_WIN[x]]),
}


with open("day_02_input.txt", encoding="utf-8") as file:
    print(
        sum(
            FUNC[result](opponent)
            for opponent, result in (line.split() for line in file)
        )
    )
