"""
At a party, there is a single person who everyone knows, but who does not know anyone in 
return (the "celebrity"). To help figure out who this is, you have access to an O(1) method 
called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
"""


def find_celebrity(people: list[list[int]]) -> int:
    length = len(people)
    candidate = 0

    for index in range(1, length):
        if people[index][candidate] == 0:
            candidate = index

    for item in people[candidate]:
        if item == 1:
            return -1

    return candidate


if __name__ == "__main__":
    _people = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
    assert find_celebrity(_people) == 2

    _people = [
        [0, 1, 0, 0],  # Person 0 knows 1, but doesn't know 2, 3, or 4
        [0, 0, 0, 0],  # Person 1 doesn't know anyone
        [0, 0, 0, 0],  # Person 2 doesn't know anyone
        [0, 0, 0, 0],  # Person 3 doesn't know anyone
        [1, 1, 1, 1],  # Person 4 knows everyone (not a celebrity)
    ]
    assert find_celebrity(_people) == 3
