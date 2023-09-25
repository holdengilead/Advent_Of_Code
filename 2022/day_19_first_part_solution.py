"""
Day 19. https://adventofcode.com/2022/day/19
"""
from __future__ import annotations

import re
from math import ceil
from typing import Optional

MAX_TIME = 24


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
                0: (cost_r_o, 0, 0),
                1: (cost_r_c, 0, 0),
                2: (cost_r_ob_o, cost_r_ob_c, 0),
                3: (cost_r_g_o, 0, cost_r_g_ob),
            }
            i += 1
    return strategies


class State:
    def __init__(self, costs, geodes=0, time=0, materials=None, robots=None) -> None:
        if materials:
            self.materials = materials
        else:
            self.materials = [0, 0, 0]
        if robots:
            self.robots = robots
        else:
            self.robots = [1, 0, 0]
        self.geodes = geodes
        self.costs = costs
        self.time = time
        self.max_robots = {i: max(self.costs[j][i] for j in range(4)) for i in range(3)}

    def can_build(self, robot_type) -> Optional[State]:
        if (
            robot_type != 3
            and self.robots[robot_type] * (MAX_TIME - self.time)
            + self.materials[robot_type]
            >= (MAX_TIME - self.time) * self.max_robots[robot_type]
        ):
            return None

        robot_costs = self.costs[robot_type]
        for i in range(3):
            if robot_costs[i] and not self.robots[i]:
                return None

        cycles = max(
            ceil((cost - material) / robot)
            for cost, material, robot in zip(robot_costs, self.materials, self.robots)
            if cost > 0
        )
        cycles = max(1, cycles + 1)
        if cycles + self.time < MAX_TIME:
            time = self.time + cycles
            materials = [
                mat + (rob * cycles) for mat, rob in zip(self.materials, self.robots)
            ]
            materials = [
                mat - cost if cost > 0 else mat
                for mat, cost in zip(materials, robot_costs)
            ]
            robots = self.robots[:]
            if robot_type == 3:
                geodes = self.geodes + (MAX_TIME - time)
            else:
                robots[robot_type] += 1
                geodes = self.geodes

            return State(
                materials=materials,
                geodes=geodes,
                robots=robots,
                costs=self.costs,
                time=time,
            )

        return None


def main(name_file: str) -> int:
    """
    Main function.
    """
    strategies = read_costs(name_file=name_file)
    quality_levels = 0

    for i in range(1, len(strategies) + 1):
        max_geodes = 0
        states = [State(costs=strategies[i])]
        while states:
            state = states.pop()
            new_robots = False
            for robot_type in range(4):
                if result := state.can_build(robot_type):
                    states.append(result)
                    new_robots = True
            if not new_robots:
                if state.geodes > max_geodes:
                    max_geodes = state.geodes

        quality_levels += i * max_geodes

    return quality_levels


if __name__ == "__main__":
    print(f'The solution to the first test part is {main("day_19_input_test.txt")}')
    print(f'The solution to the first part is {main("day_19_input.txt")}')
