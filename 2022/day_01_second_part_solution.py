"""
https://adventofcode.com/2022/day/1
"""

with open("day_01_input.txt", encoding="utf-8") as file:
    calories_carried = []
    actual_calories = 0
    for line in file:
        if line == "\n":
            calories_carried.append(actual_calories)
            actual_calories = 0
        else:
            actual_calories += int(line.strip())

print(sum(sorted(calories_carried)[-3:]))
