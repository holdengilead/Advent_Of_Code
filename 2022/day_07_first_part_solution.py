from collections import defaultdict

TREE = defaultdict(list)


def get_total_size(direc, total_sizes):
    for elem in TREE[direc]:
        if isinstance(elem, int):
            total_sizes[direc] += elem
        else:
            total_sizes[direc] += get_total_size(elem, total_sizes)
    return total_sizes[direc]


with open("day_07_input.txt", encoding="utf-8") as file:
    current = tuple()
    for line in file:
        command = line.strip().split(" ")
        if command[0] == "$" and command[1] == "cd":
            if command[2] == "..":
                current = current[:-1]
            else:
                current += (command[2],)
        elif command[0] == "dir":
            TREE[current].append(current + (command[1],))
        elif command[0].isdecimal():
            TREE[current].append(int(command[0]))

    total_sizes = defaultdict(int)
    get_total_size(("/",), total_sizes)
    print(sum(size for size in total_sizes.values() if size <= 100000))
