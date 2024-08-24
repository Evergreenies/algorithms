"""
Given a string with repeated characters, rearrange the string so that no two adjacent
characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""

import heapq

from collections import Counter


def rearrange_string(string: str) -> str | None:
    frq_count = Counter(string)
    max_heap = [(-frq, char) for char, frq in frq_count.items()]
    heapq.heapify(max_heap)
    prev_freq, prev_char = 0, ""
    result = []

    while max_heap:
        frq, char = heapq.heappop(max_heap)
        result.append(char)

        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))

        prev_freq, prev_char = frq + 1, char

    rearrange_str = "".join(result)
    for index in range(1, len(rearrange_str)):
        if rearrange_str[index] == rearrange_str[index - 1]:
            return None

    if len(rearrange_str) != len(string):
        return None

    return rearrange_str


print(rearrange_string("aaabbc"))
print(rearrange_string("aaab"))
