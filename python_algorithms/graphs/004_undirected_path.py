from collections import defaultdict
from typing import Any, DefaultDict


def undirected_graph_dfs(graph: list[list] | dict, source: Any, dest: Any) -> bool:
    if not graph:
        return False

    if source == dest:
        return True

    if isinstance(graph, list):
        graph = build_graph(graph)

    visited = defaultdict(bool)
    stack = [source]

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node == dest:
            return True

        if visited.get(current_node):
            continue

        visited[current_node] = True
        for neighbor_node in graph[current_node]:
            stack.append(neighbor_node)

    return False


def undirected_graph_dfs_recursive(
    graph: dict, source: Any, dest: Any, visited: DefaultDict
) -> bool:
    if not graph:
        return False

    if source == dest:
        return True

    for neighbor_node in graph[source]:
        if visited.get(neighbor_node):
            continue

        visited[neighbor_node] = True
        if undirected_graph_dfs_recursive(graph, neighbor_node, dest, visited) is True:
            return True

    return False


def build_graph(edges: list[list]) -> dict:
    if not edges:
        return dict()

    graph = defaultdict(list)

    for edge1, edge2 in edges:
        graph[edge1].append(edge2)
        graph[edge2].append(edge1)

    return graph


if __name__ == "__main__":
    edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
    assert undirected_graph_dfs(edges, "i", "l") is True
    assert undirected_graph_dfs(edges, "i", "o") is False
    assert undirected_graph_dfs(edges, "n", "o") is True

    assert (
        undirected_graph_dfs_recursive(build_graph(edges), "i", "l", defaultdict(bool))
        is True
    )
    assert (
        undirected_graph_dfs_recursive(build_graph(edges), "i", "o", defaultdict(bool))
        is False
    )
    assert (
        undirected_graph_dfs_recursive(build_graph(edges), "n", "o", defaultdict(bool))
        is True
    )
