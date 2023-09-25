costs = []
with open("day_7.txt", "r", encoding="utf-8") as positions:
    pos = [int(pos) for pos in positions.readline().strip().split(",")]
    for i in range(min(pos), max(pos) + 1):
        costs.append(sum(abs(p - i) * (abs(p - i) + 1) // 2 for p in pos))
print(min(costs))
