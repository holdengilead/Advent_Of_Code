"""
Day 19. https://adventofcode.com/2022/day/19
"""
import re
from math import ceil

INF = 1_000_000


def read_costs(name_file):
    strategies = {}
    i = 1
    with open(name_file, encoding="utf-8") as file:
        while line := file.readline():
            (
                _,
                cost_r_o,
                cost_r_c,
                cost_r_ob_o,
                cost_r_ob_c,
                cost_r_g_o,
                cost_r_g_ob,
            ) = map(int, re.findall("\d+", line))
            strategies[i] = {
                0: (cost_r_o, -1, -1, -1),
                1: (cost_r_c, -1, -1, -1),
                2: (cost_r_ob_o, cost_r_ob_c, -1, -1),
                3: (cost_r_g_o, -1, cost_r_g_ob, -1),
            }
            i += 1
    return strategies


def time_to_get(material, cost, robots) -> int:
    if cost == -1:
        return -1
    if not robots:
        return INF
    return max(0, ceil((cost - material) / robots))


def dont_delay(times, costs, materials, robots) -> bool:
    if not times:
        return True
    for time in times:
        old_wait = max(time[0])
        new_materials = [
            mat - cost if cost > 0 else mat for mat, cost in zip(materials, costs)
        ]
        new_wait = max(
            time_to_get(mat, cost, rob)
            for mat, cost, rob in zip(new_materials, time[1], robots)
        )
        if new_wait > old_wait:
            return False
    return True


def main(name_file: str) -> int:
    """
    Main function.
    """
    strategies = read_costs(name_file=name_file)
    quality_levels = 0

    for i in range(1, len(strategies) + 1):  # For each strategy
        materials = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        strategy = strategies[i]

        for _ in range(24):  # For each minute
            times = []
            new_robots = [0, 0, 0, 0]

            for j in (3, 2, 1, 0):  # For each robot
                costs = strategy[j]
                min_times = tuple(
                    time_to_get(mat, cost, rob)
                    for mat, cost, rob in zip(materials, costs, robots)
                )
                if not max(min_times) and dont_delay(times, costs, materials, robots):
                    new_robots[j] += 1
                    materials = [
                        mat - cost if cost > 0 else mat
                        for mat, cost in zip(materials, costs)
                    ]
                    break
                elif INF not in min_times:
                    times.append([min_times, costs])

            materials = [mat + rob for mat, rob in zip(materials, robots)]
            robots = [old + new for old, new in zip(robots, new_robots)]
        quality_levels += i * materials[-1]

    return quality_levels


if __name__ == "__main__":
    print(f'The solution to the first part is {main("day_19_input_test.txt")}')
    print(f'The solution to the first part is {main("day_19_input.txt")}')
