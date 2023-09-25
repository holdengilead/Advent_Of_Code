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
        packets = [[[2]], [[6]]]
        while True:
            try:
                packets.append(eval(file.readline().strip()))
                packets.append(eval(file.readline().strip()))
            except SyntaxError:
                break
            file.readline()
        while True:  # BubbleSort
            changes = 0
            for i in range(len(packets) - 1):
                if correct_order(packets[i], packets[i + 1]) == -1:
                    packets[i], packets[i + 1] = packets[i + 1], packets[i]
                    changes += 1
            if changes == 0:
                break
        return f"Decoder key: {(packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)}"


if __name__ == "__main__":
    print(main())
