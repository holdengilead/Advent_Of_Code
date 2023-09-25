with open("day_04_input.txt", encoding="utf-8") as file:
    pairs = 0
    for line in file:
        first, second = line.strip().split(",")
        a, b = first.split("-")
        c, d = second.split("-")
        a, b, c, d = map(int, [a, b, c, d])
        if (a <= c <= b) or (c <= a <= d):
            pairs += 1
    print(pairs)
