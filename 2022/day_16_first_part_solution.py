"""
Day 16. https://adventofcode.com/2022/day/16
"""


from collections import defaultdict
from dataclasses import dataclass

graph: dict[str, set[str]] = defaultdict(set)
distances: dict[tuple[str, str], int] = defaultdict(int)
IMP = 1_000_000


def get_distance(a: str, b: str, visited: set[str]) -> int:
    global distances

    if (a, b) in distances:
        return distances[(a, b)]
    if b in graph[a]:
        distances[(a, b)] = 1
        distances[(b, a)] = 1
        return 1
    min_dis = []
    for node in graph[a]:
        if node not in visited:
            min_dis.append(get_distance(node, b, visited | {a}))
    if not min_dis:
        return IMP
    min_dis = min(min_dis)
    if min_dis < IMP:
        distances[(a, b)] = 1 + min_dis
        distances[(b, a)] = 1 + min_dis
    return 1 + min_dis


@dataclass
class Path:
    time: int
    pos: str
    visited: set[str]
    flow: int


def test_main(name_file: str) -> None:
    """
    Main function.
    """
    global graph

    nodes_with_flow: set[str] = set()
    rates: dict[str, int] = {}
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            _, valve, _, _, rate, _, _, _, _, *edges = line.split()
            rate = int(rate[5:-1])
            edges = [node.removesuffix(",") for node in edges]
            if rate:
                nodes_with_flow.add(valve)
                rates[valve] = rate
            graph[valve].update(edges)
            for node in edges:
                graph[node].add(valve)
        possibilities = [Path(time=30, pos="AA", visited=set(), flow=0)]
        max_flow = 0
        while possibilities:
            poss_path = possibilities.pop()
            old_len = len(possibilities)
            for node in nodes_with_flow - poss_path.visited:
                time_spent = get_distance(poss_path.pos, node, set()) + 1
                if time_spent < poss_path.time:
                    possibilities.append(
                        Path(
                            time=poss_path.time - time_spent,
                            pos=node,
                            visited=poss_path.visited | {node},
                            flow=poss_path.flow
                            + (poss_path.time - time_spent) * rates[node],
                        )
                    )
            if len(possibilities) == old_len:
                max_flow = max(max_flow, poss_path.flow)
        print(max_flow)


if __name__ == "__main__":
    test_main("day_16_input_first_part_test.txt")
