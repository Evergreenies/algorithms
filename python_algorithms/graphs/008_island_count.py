from collections import defaultdict
from typing import DefaultDict


def island_count(grid: list[list]) -> int:
    if len(grid) == 0:
        return -1

    if len(grid[0]) == 0:
        return -1

    visited = defaultdict(bool)
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore_grid(grid, row, col, visited):
                count += 1

    return count


def explore_grid(grid: list, row: int, col: int, visited: DefaultDict) -> bool:
    row_inbound = 0 <= row < len(grid)
    col_inbound = 0 <= col < len(grid[0])

    if not row_inbound or not col_inbound:
        return False

    if grid[row][col] == "w":
        return False

    position = (row, col)
    if visited.get(position):
        return False

    visited[position] = True

    explore_grid(grid, row - 1, col, visited)
    explore_grid(grid, row + 1, col, visited)
    explore_grid(grid, row, col - 1, visited)
    explore_grid(grid, row, col + 1, visited)

    return True


if __name__ == "__main__":
    grid = [
        ["w", "l", "w", "w", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "w", "w", "l", "l"],
        ["l", "l", "w", "w", "w"],
    ]
    assert island_count(grid) == 3

    grid = [
        ["l", "l", "l"],
        ["l", "l", "l"],
        ["l", "l", "l"],
    ]
    assert island_count(grid) == 1

    grid = [
        ["w", "w", "w"],
        ["w", "w", "w"],
        ["w", "w", "w"],
    ]
    assert island_count(grid) == 0
