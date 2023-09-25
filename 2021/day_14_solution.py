# from collections import Counter

# with open("day_14.txt") as _input:
#     polymer = _input.readline().strip()
#     _input.readline()
#     rules = {}
#     for _ in range(100):
#         pair, insert = _input.readline().strip().split(" -> ")
#         rules[pair] = insert
#     for step in range(40):
#         print(f"Step {step}")
#         aux = (rules[polymer[i] + polymer[i + 1]] for i in range(0, len(polymer) - 1))
#         polymer = "".join((a + b for a, b in zip(polymer, aux))) + polymer[-1]

#     freq = Counter(polymer)
#     freq = freq.most_common()
#     print(freq[0][1] - freq[-1][1])


from math import ceil


with open("day_14.txt") as _input:
    polymer = _input.readline().strip()
    _input.readline()
    rules = {}
    pairs = {}
    for _ in range(100):
        pair, insert = _input.readline().strip().split(" -> ")
        rules[pair] = (pair[0] + insert, insert + pair[1])
        pairs[pair] = 0
    for i in range(len(polymer) - 1):
        pairs[polymer[i] + polymer[i + 1]] += 1
    for step in range(40):
        for k, v in list(pairs.items()):
            if v > 0:
                pairs[k] -= v
                pairs[rules[k][0]] += v
                pairs[rules[k][1]] += v
    freq = {}
    for k, v in pairs.items():
        freq[k[0]] = freq.get(k[0], 0) + v
        freq[k[1]] = freq.get(k[1], 0) + v

    print(ceil(max(freq.values()) / 2) - ceil(min(freq.values()) / 2))
