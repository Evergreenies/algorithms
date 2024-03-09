from collections import defaultdict
from typing import Any, Dict


def explore_graph(graph: dict, current: Any, visited: dict) -> bool:
    if visited.get(current):
        return False

    visited[current] = True
    for neighbor_node in graph[current]:
        explore_graph(graph, neighbor_node, visited)

    return True


def connected_components(graph: Dict) -> int:
    count = 0
    visited = defaultdict(bool)

    for node in graph:
        if explore_graph(graph, node, visited) is True:
            count += 1

    return count


if __name__ == "__main__":
    _graph = {
        0: [8, 5, 1],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    assert connected_components(_graph) == 2
