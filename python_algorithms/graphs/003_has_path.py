from typing import Any


def has_path_dfs_recursive(graph: dict, source: Any, dest: Any) -> bool:
    if not graph:
        return False
    if source == dest:
        return True

    for neighbor_node in graph[source]:
        if has_path_dfs_recursive(graph, neighbor_node, dest) is True:
            return True

    return False


def has_path_dfs_stack(graph: dict, source: Any, dest: Any) -> bool:
    if not graph:
        return False

    if source == dest:
        return True

    stack = [source]
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node == dest:
            return True

        for neighbor_node in graph[current_node]:
            stack.append(neighbor_node)

    return False


def has_path_bfs(graph: dict, source: Any, dest: Any) -> bool:
    if not graph:
        return False
    if source == dest:
        return True

    queue = [source]
    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node == dest:
            return True

        for neighbor_node in graph[current_node]:
            queue.append(neighbor_node)

    return False


if __name__ == "__main__":
    # INFO: non cyclick graph input only
    _graph = {
        "f": ["g", "i"],
        "g": ["h"],
        "h": [],
        "i": ["g", "k"],
        "j": ["i"],
        "k": [],
    }
    assert has_path_dfs_recursive(_graph, "f", "k") is True
    assert has_path_dfs_recursive(_graph, "f", "j") is False

    assert has_path_dfs_stack(_graph, "f", "k") is True
    assert has_path_dfs_stack(_graph, "f", "j") is False

    assert has_path_bfs(_graph, "f", "j") is False
    assert has_path_bfs(_graph, "f", "k") is True
