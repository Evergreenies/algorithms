from collections import defaultdict
from typing import Any, DefaultDict, Dict


def explore_graph(graph: Dict, current_node: Any, visited: DefaultDict) -> int:
    if visited.get(current_node):
        return 0

    length = 1
    visited[current_node] = True
    for neighbour_node in graph[current_node]:
        length += explore_graph(graph, neighbour_node, visited)

    return length


def largest_component(graph: Dict) -> int:
    largest_component_length = 0

    for current_node in graph:
        length = explore_graph(graph, current_node, defaultdict(bool))

        if length > largest_component_length:
            largest_component_length = length

    return largest_component_length


if __name__ == "__main__":
    _graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    assert largest_component(_graph) == 4
