from typing import Any


def has_path_dfs_recursive(graph: dict, source: Any, dest: Any) -> bool:
    if not graph:
        return False
    if source == dest:
        return True

    for neighbor_node in graph[source]:
        if has_path_dfs_recursive(graph, neighbor_node, dest) == True:
            return True

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
    assert has_path_dfs_recursive(_graph, "f", "k") == True
    assert has_path_dfs_recursive(_graph, "f", "j") == False
