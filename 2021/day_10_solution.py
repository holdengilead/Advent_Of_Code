# from collections import deque

# start = {"(": ")", "[": "]", "{": "}", "<": ">"}
# stack = deque()
# points = {")": 3, "]": 57, "}": 1197, ">": 25137}
# total = 0
# with open("day_10.txt", "r", encoding="utf-8") as lines:
#     for line in lines:
#         line = line.strip()
#         for chunk in line:
#             if chunk in start:
#                 stack.append(chunk)
#             else:
#                 aux = stack.pop()
#                 if start[aux] != chunk:
#                     total += points[chunk]
#                     break

# print(total)


from collections import deque

start = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {"(": 1, "[": 2, "{": 3, "<": 4}
total = []
with open("day_10.txt", "r", encoding="utf-8") as lines:
    for line in lines:
        stack = deque()
        CORRUPTED = False
        line = line.strip()
        for chunk in line:
            if chunk in start:
                stack.append(chunk)
            else:
                aux = stack.pop()
                if start[aux] != chunk:
                    CORRUPTED = True
                    break
        if not CORRUPTED:
            SCORE = 0
            while len(stack) > 0:
                SCORE *= 5
                SCORE += points[stack.pop()]
            total.append(SCORE)

total.sort()
print(total[len(total) // 2])
