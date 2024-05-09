"""
Recall that the minimum spanning tree is the subset of edges of a tree that connect all 
its vertices with the smallest possible total edge weight. Given an undirected graph with 
weighted edges, compute the maximum weight spanning tree.
"""

from heapq import heappop, heappush


def max_spanning_tree(graph: dict[int, dict], vertex: int):
    mst = set()
    total_weight = 0
    pq = [(0, vertex)]

    while pq:
        weight, u = heappop(pq)
        if u not in mst:
            mst.add(u)
            total_weight += weight

            for v, endge_weight in graph[u].items():
                heappush(pq, (max(float("-inf"), endge_weight), v))

    return mst, total_weight


if __name__ == "__main__":
    graph = {
        1: {2: 4, 3: 2},
        2: {1: 4, 4: 3, 5: 1},
        3: {1: 2, 4: 7},
        4: {2: 3, 3: 7, 5: 5},
        5: {2: 1, 4: 5},
    }
    print(max_spanning_tree(graph, 1))
