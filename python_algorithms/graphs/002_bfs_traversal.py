# BFS traversal

from typing import Any


def bfs_traversal(graph: dict, start: Any) -> list:
    if not graph:
        return []

    traversed = []
    queue = [start]

    while len(queue) > 0:
        current_node = queue.pop(0)
        traversed.append(current_node)

        for neighbor_node in graph[current_node]:
            queue.append(neighbor_node)

    return traversed


if __name__ == "__main__":
    _graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    assert bfs_traversal(_graph, "a") == ["a", "b", "c", "d", "e", "f"]
