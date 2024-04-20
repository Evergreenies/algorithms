"""
Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine 
whether each vertex in the graph can be colored such that no two adjacent vertices share the same color 
using at most k colors.
"""


def is_safe(graph: list[list], vertex: int, color: int, colors: list[int]) -> bool:
    for neighbor in range(len(graph[vertex])):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False

    return True


def dfs(graph: list[list], vertex: int, k: int, colors: list[int]) -> bool:
    if vertex == len(graph):
        return True

    for assigned_color in range(1, k + 1):
        if is_safe(graph, vertex, assigned_color, colors):
            colors[vertex] = assigned_color

            if dfs(graph, vertex + 1, k, colors):
                return True

            colors[vertex] = 0

    return False


def is_k_colorable(graph: list[list], k: int) -> bool:
    colors = [0 for _ in range(len(graph))]

    if dfs(graph, 0, k, colors):
        return True

    return False


if __name__ == "__main__":
    _graph = [
        [0, 1, 1, 1],  # Adjacency matrix representation
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]

    assert is_k_colorable(_graph, 3) is True
