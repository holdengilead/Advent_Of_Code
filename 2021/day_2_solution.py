dict_movements = {"forward": 0, "up": 0, "down": 0}
with open("day_2.txt", "r", encoding="utf-8") as movements:
    for move in movements:
        move_type, value = move.split(" ")
        dict_movements[move_type] += int(value)

print(
    f"The solution to the first part is: {dict_movements['forward'] * (dict_movements['down'] - dict_movements['up'])}"
)

print("*-*" * 35)

aim = 0
pos = 0
depth = 0
with open("day_2.txt", "r", encoding="utf-8") as movements:
    for move in movements:
        move_type, value = move.split(" ")
        if move_type == "down":
            aim += int(value)
        elif move_type == "up":
            aim -= int(value)
        else:
            pos += int(value)
            depth += aim * int(value)

print(f"The solution to the second part is: {pos * depth}")
