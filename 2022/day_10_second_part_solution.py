with open("day_10_input.txt", encoding="utf-8") as file:
    cycle = 1
    reg_x = 1
    active_add = False
    value_add = 0
    while cycle <= 240:
        if (cycle - 1) % 40 in (reg_x - 1, reg_x, reg_x + 1):
            print("#", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
        if active_add:
            reg_x += value_add
            active_add = False
        else:
            op = file.readline().strip()
            if op[0] == "a":
                active_add = True
                value_add = int(op.split()[1])
        cycle += 1
