"""
A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends
with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
Each student can be placed in a friend group, which can be defined as the transitive closure
of that student's friendship relations. In other words, this is the smallest set such that no
student in the group has any friends outside this group. For the example above, the friend groups
would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""

from typing import Any


def search_group_dfs(
    student: Any, friendship: dict[Any, list[Any]], visited: set[Any], group: set[Any]
) -> set[Any] | None:
    if student in visited:
        return

    visited.add(student)
    group.add(student)
    for friend in friendship[student]:
        search_group_dfs(friend, friendship, visited, group)

    return group


def get_friends_group(friendship: dict[Any, list[Any]]) -> int:
    groups_count, visited, groups = 0, set(), list()

    for student in friendship:
        if student not in visited:
            friends_group = search_group_dfs(student, friendship, visited, set())
            if friends_group:
                groups.append(friends_group)

            groups_count += 1

    print(f"{groups=}")
    return groups_count


if __name__ == "__main__":
    friendships = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}

    assert get_friends_group(friendships) == 3
