"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents
land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter
is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def find_islands(matrix: list[list]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows, columns = len(matrix), len(matrix[0])
    visited = [[False for _ in range(columns)] for _ in range(rows)]

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= columns:
            return

        if matrix[row][col] == 0 or visited[row][col]:
            return

        visited[row][col] = True

        # explore all neighboring elements
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    island_count = 0
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == 1 and not visited[row][col]:
                dfs(row, col)
                island_count += 1

    return island_count


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]
    assert find_islands(matrix) == 4
