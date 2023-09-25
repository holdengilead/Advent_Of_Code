class Monkey:
    def __init__(self, items: str, operation, test, true_cond, false_cond) -> None:
        self.items = [int(item) for item in items.replace(",", "").split()]
        self.operation = operation.split()
        self.test = int(test)
        self.true_cond = true_cond
        self.false_cond = false_cond
        self.items_inspected = 0

    def play(self, item: int):
        self.items_inspected += 1
        operator = int(self.operation[1]) if self.operation[1].isnumeric() else item
        if self.operation[0] == "+":
            item = item + operator
        else:
            item = item * operator
        item = item // 3
        if item % self.test == 0:
            return self.true_cond, item
        return self.false_cond, item


class Jungle:
    def __init__(self) -> None:
        self.monkeys: dict[str, Monkey] = {}

    def add(self, num_monkey, monkey):
        self.monkeys[num_monkey[:-1]] = monkey


jungle = Jungle()

with open("day_11_input.txt", encoding="utf-8") as file:
    while line := file.readline().strip():
        _, num_monkey = line.split()
        line = file.readline().strip()
        _, items = line.split(":")
        line = file.readline().strip()
        _, operation = line.split(":")
        operation = operation[operation.index("d") + 2 :]
        line = file.readline().strip()
        *_, test = line.split()
        line = file.readline().strip()
        *_, _true = line.split()
        line = file.readline().strip()
        *_, _false = line.split()
        file.readline()
        jungle.add(num_monkey, Monkey(items, operation, test, _true, _false))


for _ in range(20):
    for _, monkey in jungle.monkeys.items():
        while True:
            if monkey.items:
                item = monkey.items.pop(0)
                dest, item = monkey.play(item)
                jungle.monkeys[dest].items.append(item)
            else:
                break

*_, second, first = sorted(jungle.monkeys.values(), key=lambda x: x.items_inspected)
print(f"Monkey business: {first.items_inspected * second.items_inspected}")
