"""
A teacher must divide a class of students into two teams to play dodgeball. Unfortunately,
not all the kids get along, and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory
pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
On the other hand, given the input below, you should return False.

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
"""

from collections import deque


def bfs(start: int, color: dict, students: dict) -> bool:
    queue = deque([start])
    color[start] = 0

    while queue:
        node = queue.popleft()
        current_color = color[node]

        for neighbor in students[node]:
            if color.get(neighbor) is None:
                color[neighbor] = 1 - current_color
                queue.append(neighbor)
            elif color.get(neighbor) == current_color:
                return False

    return True


def can_divide_teams(students: dict) -> tuple | bool:
    color = dict()

    for student in students:
        if color.get(student) is None:
            if not bfs(student, color, students):
                return False

    team1 = [student for student in students if color[student] == 0]
    team2 = [student for student in students if color[student] == 1]

    return team1, team2


# Example 1:
students1 = {0: [3], 1: [2], 2: [1, 4], 3: [0, 4, 5], 4: [2, 3], 5: [3]}
print(can_divide_teams(students1))  # Should return the two teams

# Example 2:
students2 = {0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4, 5], 4: [2, 3], 5: [3]}
print(can_divide_teams(students2))  # Should return False
