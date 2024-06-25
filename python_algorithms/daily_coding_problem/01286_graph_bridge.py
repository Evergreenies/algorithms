"""
A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become
disconnected. Find all the bridges in a graph.
"""


class Graph:
    def __init__(self, num_vertices) -> None:
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        self.visited = [False] * num_vertices
        self.low = [0] * num_vertices
        self.disc = [0] * num_vertices
        self.parent = [-1] * num_vertices
        self.time = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_bridges(self, u):
        self.time += 1
        self.visited[u] = True
        self.disc[u] = self.low[u] = self.time

        for v in self.adj_list[u]:
            if not self.visited[v]:
                self.parent[v] = u
                self.find_bridges(v)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] > self.disc[u]:
                    print(f"Bridge: ({u}, {v})")
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])


graph = Graph(5)
graph.add_edge(1, 0)
graph.add_edge(0, 2)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.find_bridges(0)
