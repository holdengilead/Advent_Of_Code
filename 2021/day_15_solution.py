from dijkstar import Graph, find_path

cave = {}
with open("day_15.txt") as f:
    for i in range(100):
        line = f.readline().strip()
        for j in enumerate(line):
            cave[(i, j[0])] = int(j[1])

for i in range(500):
    for j in range(500):
        cost = cave[(i % 100, j % 100)] + i // 100 + j // 100
        if cost > 9:
            cost = cost % 10 + 1
        cave[(i, j)] = cost

# UN APAÑO QUE HE HECHO
# path = [[[(0, 0)], 0]]
# min_cost = 9999999
# while path:
#     current = path.pop()
#     if current[1] >= min_cost:
#         pass
#     elif current[0][-1] == (9, 9):
#         print(f"I found a path with a cost of {current[1]}")
#         min_cost = current[1]
#     else:
#         for mov in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#             aux = deepcopy(current)
#             next_pos = (aux[0][-1][0] + mov[0], aux[0][-1][1] + mov[1])
#             if next_pos in cave and next_pos not in aux[0]:
#                 aux[0].append(next_pos)
#                 aux[1] += cave[next_pos]
#                 path.append(aux)

# LA PRIMERA PARTE
# graph = Graph()
# for i in range(100):
#     for j in range(100):
#         for mov in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#             from_pos = (i + mov[0], j + mov[1])
#             if from_pos in cave:
#                 graph.add_edge(from_pos, (i, j), cave[(i, j)])

# path_info = find_path(graph, (0, 0), (99, 99))
# print(path_info.total_cost)

graph = Graph()
for i in range(500):
    for j in range(500):
        for mov in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            from_pos = (i + mov[0], j + mov[1])
            if from_pos in cave:
                graph.add_edge(from_pos, (i, j), cave[(i, j)])

path_info = find_path(graph, (0, 0), (499, 499))
print(path_info.total_cost)
