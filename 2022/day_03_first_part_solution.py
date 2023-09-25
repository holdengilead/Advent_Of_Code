with open("day_03_input.txt", encoding="utf-8") as file:
    sum_priorities = 0
    for line in file:
        s_line = line.strip()
        half = len(s_line) // 2
        error: str = set(s_line[:half]).intersection(set(s_line[half:])).pop()
        sum_priorities += ord(error) - (96 if error.islower() else 38)
    print(sum_priorities)
