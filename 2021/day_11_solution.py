import sys


def to_print(aa):
    for ii in range(10):
        for jj in range(10):
            # print(aa[(i, j)], end="")
            print("{0:3d}".format(aa[(ii, jj)]), end="")
        print()
    input()


moves = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)

with open("day_11.txt", "r", encoding="utf-8") as input_:
    energies = dict()
    for i in range(10):
        line = list(input_.readline().strip())
        for j, value in enumerate(line):
            energies[(i, j)] = int(value)
    # to_print(energies)
    FLASHES = 0
    for _ in range(1000):
        print(_, sum(energies.values()))
        if sum(energies.values()) == 0:
            sys.exit()
        to_flash = set()
        # print(f"to_flash --> {to_flash}")
        for i in range(10):
            for j in range(10):
                energies[(i, j)] += 1
                if energies[(i, j)] > 9:
                    to_flash.add((i, j))
                    # print(f"to_flash --> {to_flash}")
        # to_print(energies)
        while to_flash:
            to_process = to_flash.pop()
            FLASHES += 1
            # print(f"to_flash --> {to_flash}")
            # print(f"El nodo a flashear es: {to_process}")
            for mov in moves:
                aux = (to_process[0] + mov[0], to_process[1] + mov[1])
                if aux in energies and energies[aux] != 0:
                    energies[aux] += 1
                    if energies[aux] > 9:
                        to_flash.add(aux)
                        # print(f"to_flash --> {to_flash}")
            energies[to_process] = 0
            # to_print(energies)

print(FLASHES)
