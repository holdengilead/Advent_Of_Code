with open("day_10_input.txt", encoding="utf-8") as file:
    cycle = 1
    reg_x = 1
    OBJECTIVES = (20, 60, 100, 140, 180, 220)
    signals = 0
    active_add = False
    value_add = 0
    while cycle <= 220:
        if cycle in OBJECTIVES:
            signals += cycle * reg_x
        if active_add:
            reg_x += value_add
            active_add = False
        else:
            op = file.readline().strip()
            if op[0] == "a":
                active_add = True
                value_add = int(op.split()[1])
        cycle += 1
    print(f"Sum of signal strength: {signals}")
