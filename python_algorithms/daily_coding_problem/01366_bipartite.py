"""
Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite
if its vertices can be divided into two independent sets, U and V, such that no edge connects
vertices of the same set.
"""

from collections import deque


def is_bipartite(graph):
    # Step 1: Create a list to store the color of each vertex (-1 means uncolored)
    n = len(graph)  # number of vertices
    color = [-1] * n

    # Step 2: Try to color each component of the graph (some graphs may be disconnected)
    for start in range(n):
        if color[start] == -1:  # If the vertex hasn't been colored, we color it
            # Step 3: Start BFS from this vertex
            queue = deque([start])
            color[start] = 0  # Start with color 0

            while queue:
                node = queue.popleft()

                # Step 4: Check all adjacent vertices
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Color with opposite color
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # A conflict is found
                        return False
    return True


# Example usage:
# Graph represented as adjacency list:
# 0 -- 1
#  \   /
#   2
graph = [
    [1, 2],  # Node 0 is connected to nodes 1 and 2
    [0, 2],  # Node 1 is connected to nodes 0 and 2
    [
        0,
        1,
    ],  # Node 2 is connected to nodes 0 and 1 (This forms an odd cycle, so it's not bipartite)
]

print(is_bipartite(graph))  # Output: False
