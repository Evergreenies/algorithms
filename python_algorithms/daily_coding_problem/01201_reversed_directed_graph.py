"""
Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""

from collections import defaultdict
from typing import Any


def reversed_graph(graph: dict[Any, list]) -> dict[Any, list]:
    reversed_graph_dict = defaultdict(list)
    for vertex, neighbors in graph.items():
        if not reversed_graph_dict.get(vertex):
            reversed_graph_dict[vertex] = []

        for neighbor in neighbors:
            reversed_graph_dict[neighbor].append(vertex)

    return reversed_graph_dict


if __name__ == "__main__":
    original_graph = {"A": ["B", "C"], "B": ["C"], "C": []}
    assert reversed_graph(original_graph) == {"A": [], "B": ["A"], "C": ["A", "B"]}
