from itertools import zip_longest


def correct_order(first, second):
    for left, right in zip_longest(first, second):
        if left is None:
            return 1
        if right is None:
            return -1
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            if left > right:
                return -1
            continue
        left = left if isinstance(left, list) else [left]
        right = right if isinstance(right, list) else [right]
        rec = correct_order(left, right)
        if rec == 1:
            return 1
        if rec == -1:
            return -1


def main():
    with open("day_13_input.txt", encoding="utf-8") as file:
        sum_indeces = 0
        index = 1
        while True:
            try:
                first, second = (eval(file.readline().strip()) for _ in range(2))
            except SyntaxError:
                return sum_indeces
            file.readline()
            if correct_order(first, second) == 1:
                sum_indeces += index
            index += 1


if __name__ == "__main__":
    print(main())
