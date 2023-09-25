prev = -1
incs = 0
with open("day_1.txt", "r", encoding="utf-8") as depths:
    for depth in depths:
        if int(depth) > prev:
            incs += 1
        prev = int(depth)

print(f"The solution to the first part is: {incs - 1}")

print("*-*" * 35)

incs = 0
depths = [int(depth) for depth in open("day_1.txt", "r", encoding="utf-8")]
prev = sum(depths[:3])
for i in range(3, len(depths)):
    aux = sum(depths[i - 2 : i + 1])
    if aux > prev:
        incs += 1
    prev = aux

print(f"The solution to the second part is: {incs}")
