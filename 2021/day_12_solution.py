# from collections import defaultdict

# graph = defaultdict(list)
# with open("day_12.txt") as paths:
#     for path in paths:
#         path = path.strip()
#         a, b = path.split("-")
#         graph[a].append(b)
#         graph[b].append(a)

# paths = [["start"]]
# num_paths = 0
# while paths:
#     # print(paths)
#     # input()
#     path = paths.pop()
#     # print(paths)
#     # input()
#     if path[-1] == "end":
#         num_paths += 1
#     else:
#         for possible in graph[path[-1]]:
#             if possible.isupper() or possible not in path:
#                 paths.append(path + [possible])
#                 # print(paths)
#                 # input()

# print(num_paths)


from collections import defaultdict

graph = defaultdict(list)
with open("day_12.txt") as paths:
    for path in paths:
        path = path.strip()
        a, b = path.split("-")
        graph[a].append(b)
        graph[b].append(a)

paths = [[False, "start"]]
num_paths = 0
while paths:
    # print(f"PATHS: {paths}")
    path = paths.pop()
    # print(f"Path a investigar: {path}")
    if path[-1] == "end":
        num_paths += 1
        # print("PATH COMPLETO")
    else:
        for possible in graph[path[-1]]:
            # print(f"POSSIBLE: {possible}")
            if possible.isupper():
                paths.append(path + [possible])
                # print("AÑADO POR SER MAYUSCULA")
            else:
                if possible not in path:
                    paths.append(path + [possible])
                    # print("AÑADO POR NO ESTAR")
                elif possible != "start" and not path[0]:
                    aux_path = path[:]
                    aux_path[0] = True
                    paths.append(aux_path + [possible])
                    # print("AÑADO POR SER LA PRIMERA REPETICIÓN")
                # else:
                # print(
                #     "NO AÑADO POR SER start o porque es minuscula y ya hay un repe"
                # )
            # input()

print(num_paths)
