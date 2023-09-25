from collections import defaultdict, deque


class Stacks:
    def __init__(self, file) -> None:
        self._stacks = defaultdict(list)
        for _ in range(8):
            line = file.readline()
            j = 1
            for i in range(1, 10):
                crate = line[j]
                if crate != " ":
                    self._stacks[i].append(crate)
                j += 4
        self.stacks = {i + 1: deque() for i in range(9)}
        for stack, crates in self._stacks.items():
            for crate in crates[::-1]:
                self.stacks[stack].append(crate)

    def process_movement(self, movement: str):
        _, number, _, origin, _, destiny = movement.split(" ")
        for _ in range(int(number)):
            self.stacks[int(destiny)].append(self.stacks[int(origin)].pop())

    def get_top(self):
        return "".join(self.stacks[i].pop() for i in range(1, 10))


def main():
    with open("day_05_input.txt", encoding="utf-8") as file:
        stacks = Stacks(file)
        file.readline()
        file.readline()
        for line in file:
            stacks.process_movement(line)
        print(stacks.get_top())


if __name__ == "__main__":
    main()
