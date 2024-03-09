from typing import Any, Dict
from collections import defaultdict


def shortest_path(graph: Dict, source: Any, dest: Any) -> int:
    if not graph:
        return -1

    queue: list[tuple[Any, int]] = [(source, 0)]
    visited = defaultdict(bool)

    while len(queue) > 0:
        current_node, distance = queue.pop(0)

        if visited.get(current_node):
            continue

        visited[current_node] = True
        if current_node == dest:
            return distance

        for neighbour_node in graph[current_node]:
            queue.append((neighbour_node, distance + 1))

    return -1


def build_graph(edges: list[list]) -> Dict:
    graph = defaultdict(list)

    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


if __name__ == "__main__":
    _edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
    assert shortest_path(build_graph(_edges), "w", "z") == 2
