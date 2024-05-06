"""
Given a start word, an end word, and a dictionary of valid words, find the shortest transformation 
sequence from start to end such that only one letter is changed at each step of the sequence, and 
each transformed word exists in the dictionary. If there is no possible transformation, return null. 
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, 
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there 
is no possible transformation from dog to cat.
"""
from collections import deque


def find_shortest_transformation(start: str, end: str, dictionary: list[str]):
    if start == end:
        return []

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        word, transformations = queue.popleft()
        visited.add(word)

        for index in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:index] + char + word[index + 1 :]
                if new_word == end:
                    return transformations + [new_word]

                if new_word not in visited and new_word in dictionary:
                    queue.append((new_word, transformations + [new_word]))

    return


if __name__ == "__main__":
    assert find_shortest_transformation("dog", "cat", ["dot", "dop", "dat", "cat"]) == [
        "dog",
        "dot",
        "dat",
        "cat",
    ]
