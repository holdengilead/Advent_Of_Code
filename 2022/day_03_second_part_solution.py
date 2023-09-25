with open("day_03_input.txt", encoding="utf-8") as file:
    sum_priorities = 0
    while True:
        a = file.readline().strip()
        b = file.readline().strip()
        c = file.readline().strip()
        if not a:
            print(sum_priorities)
            break
        else:
            s_error = set(a) & set(b) & set(c)
            error = s_error.pop()
            sum_priorities += ord(error) - (96 if error.islower() else 38)
