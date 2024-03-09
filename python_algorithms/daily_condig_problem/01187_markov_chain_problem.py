"""
You are given a starting state start, a list of transition probabilities 
for a Markov chain, and a number of steps num_steps. Run the Markov chain 
starting from start for num_steps and compute the number of times we 
visited each state.

For example, given the starting state a, number of steps 5000, and the 
following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce 
{ 'a': 3012, 'b': 1656, 'c': 332 }
"""
from random import random
from collections import defaultdict
from typing import Any, Union


class GraphDirectedWeighted:
    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        if node not in self.connections.keys():
            self.connections[node] = {}
            self.nodes += 1

    def add_edge(
        self, node1: Union[int, str], node2: Union[int, str], weight: int | float
    ) -> None:
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight


def get_transition(graph: GraphDirectedWeighted, node: Any) -> Any:
    transition = random()
    current = 0
    for neighbour in graph.connections[node]:
        current += graph.connections[node][neighbour]
        if current >= transition:
            return neighbour


def markov_chain(transitions: list[tuple], source: Any, steps: int) -> dict:
    graph = GraphDirectedWeighted()

    for node1, node2, probability in transitions:
        graph.add_edge(node1, node2, probability)

    visited = defaultdict(int)
    node = source

    for _ in range(steps):
        node = get_transition(graph, node)
        visited[node] += 1

    return visited


if __name__ == "__main__":
    _edges = [
        ("a", "a", 0.9),
        ("a", "b", 0.075),
        ("a", "c", 0.025),
        ("b", "a", 0.15),
        ("b", "b", 0.8),
        ("b", "c", 0.05),
        ("c", "a", 0.25),
        ("c", "b", 0.25),
        ("c", "c", 0.5),
    ]
    print(markov_chain(_edges, "a", 5000))
