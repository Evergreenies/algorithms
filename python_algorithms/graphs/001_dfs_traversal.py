# Depth first traversal


from typing import Any


def dfs_traversal_stack(graph: dict, start: str) -> list:
    if graph is None:
        return []

    stack = [start]
    traversed = []
    while len(stack) > 0:
        current = stack.pop()
        traversed.append(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

    return traversed


def dfs_traversal_recursive(graph: dict, start: Any, traversed: list) -> list:
    if graph is None:
        return []

    traversed.append(start)
    for neighbor in graph[start]:
        dfs_traversal_recursive(graph, neighbor, traversed)

    return traversed


if __name__ == "__main__":
    _graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    assert dfs_traversal_stack(_graph, "a") == ["a", "c", "e", "b", "d", "f"]
    assert dfs_traversal_recursive(_graph, "a", []) == ["a", "b", "d", "f", "c", "e"]
