"""
The transitive closure of a graph is a measure of which vertices are reachable from other vertices.
It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j,
and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""


def transitive_closure(graph: list[list]) -> list[list]:
    length = len(graph)
    closure = [[0] * length for _ in range(length)]

    for index in range(length):
        closure[index][index] = 1

    for index_i in range(length):
        for index_j in graph[index_i]:
            closure[index_i][index_j] = 1

    for index_k in range(length):
        for index_i in range(length):
            for index_j in range(length):
                closure[index_i][index_j] = closure[index_i][index_j] or (
                    closure[index_i][index_k] and closure[index_k][index_j]
                )

    return closure


graph = [[0, 1, 3], [1, 2], [2], [3]]

# Compute the transitive closure
closure_matrix = transitive_closure(graph)

# Print the result
for row in closure_matrix:
    print(" |", row, end=" |\n")
