"""
https://adventofcode.com/2022/day/1
"""

with open("day_01_input.txt", encoding="utf-8") as file:
    max_calories = -1
    actual_calories = 0
    for line in file:
        if line == "\n":
            max_calories = max(max_calories, actual_calories)
            actual_calories = 0
        else:
            actual_calories += int(line.strip())

print(max(actual_calories, max_calories))
