from collections import Counter

with open("day_6.txt", "r", encoding="utf-8") as num_fish:
    fish = Counter([int(n) for n in num_fish.readline().strip().split(",")])
    for d in range(256):
        aux = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[6] += aux
        fish[8] = aux

    print(sum(fish.values()))
