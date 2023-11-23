"""
Day 13 - 2020. https://adventofcode.com/2020/day/13#part2
"""


from functools import reduce


def chinese_remainder(m, a):
    summation = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        summation += a_i * mul_inv(p, n_i) * p
    return summation % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main(name_file: str) -> int:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        file.readline()
        buses = file.readline().strip().split(",")
        m = [int(buses[0])]
        a = [0]
        for pos, bus_id in enumerate(buses[1:], start=1):
            if bus_id != "x":
                m.append(int(bus_id))
                a.append(int(bus_id) - pos)
        return chinese_remainder(m, a)


if __name__ == "__main__":
    test_solution = main("2020/day_13_2020_first_part_test_input.txt")
    assert test_solution == 1068781
    print(
        f'The solution to the second part is {main("2020/day_13_2020_first_part_input.txt")}'
    )
