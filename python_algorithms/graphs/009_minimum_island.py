import math
from collections import defaultdict
from typing import DefaultDict


def minimum_island(grid: list[list]) -> int | float:
    if len(grid) == 0:
        return -1

    if len(grid[0]) == 0:
        return -1

    visited = defaultdict(bool)
    smallest_island = math.inf

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore_island(grid, row, col, visited)
            if 0 < size < smallest_island:
                smallest_island = size

    return int(smallest_island) if smallest_island != math.inf else math.inf


def explore_island(grid: list[list], row: int, col: int, visited: DefaultDict) -> int:
    if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
        return 0

    if grid[row][col] == "w":
        return 0

    position = (row, col)
    if visited.get(position):
        return 0

    visited[position] = True
    size = 1

    size += explore_island(grid, row - 1, col, visited)
    size += explore_island(grid, row + 1, col, visited)
    size += explore_island(grid, row, col - 1, visited)
    size += explore_island(grid, row, col + 1, visited)

    return size


if __name__ == "__main__":
    grid = [
        ["w", "l", "w", "w", "w"],
        ["w", "l", "w", "w", "w"],
        ["w", "w", "w", "l", "w"],
        ["w", "w", "l", "l", "w"],
        ["l", "w", "w", "l", "l"],
        ["l", "l", "w", "w", "w"],
    ]
    assert minimum_island(grid) == 2

    grid = [
        ["l", "l", "l"],
        ["l", "l", "l"],
        ["l", "l", "l"],
    ]
    assert minimum_island(grid) == 9

    grid = [
        ["w", "w", "w"],
        ["w", "w", "w"],
        ["w", "w", "w"],
    ]
    assert minimum_island(grid) == math.inf
