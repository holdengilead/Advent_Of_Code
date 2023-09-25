def fold_x(dots, fold):
    new_dots = set()
    for dot in dots:
        if dot[0] < fold:
            new_dots.add(dot)
        elif dot[0] > fold:
            new_dots.add((fold - (dot[0] - fold), dot[1]))
    return new_dots


def fold_y(dots, fold):
    new_dots = set()
    for dot in dots:
        if dot[1] < fold:
            new_dots.add(dot)
        elif dot[1] > fold:
            new_dots.add((dot[0], (fold - (dot[1] - fold))))
    return new_dots


if __name__ == "__main__":
    dots = set()
    with open("day_13.txt") as input_:
        for _ in range(908):
            x, y = input_.readline().strip().split(",")
            dots.add((int(x), int(y)))
        input_.readline()

        for _ in range(12):
            axis, number = input_.readline().strip().split("=")
            if axis[-1] == "x":
                dots = fold_x(dots, int(number))
            else:
                dots = fold_y(dots, int(number))

    for j in range(10):
        for i in range(50):
            if (i, j) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()
