"""
Find an efficient algorithm to find the smallest distance (measured in number of words) 
between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat 
dog dog hello cat world", return 1 because there's only one word "cat" in between the 
two words.
"""


def find_smallest_distance(string: str, start: str, end: str) -> int:
    if not string:
        return -1

    if not start or not end:
        return -1

    lst = string.split(" ")
    length = len(lst)
    start_index, smallest_distance = 0, length

    while start_index < length - 1:
        end_index = start_index + 1

        if lst[start_index] == start and lst[end_index] == end:
            return end_index - start_index - 1

        if lst[start_index] == start:
            while end_index < length and start_index < end_index:
                if lst[end_index] == start:
                    start_index = end_index
                    end_index += 1

                if lst[end_index] == end:
                    distance = end_index - start_index - 1
                    if distance < smallest_distance:
                        smallest_distance = distance

                end_index += 1
        start_index += 1

    return smallest_distance


if __name__ == "__main__":
    assert (
        find_smallest_distance(
            "dog cat hello cat dog dog hello cat world", "hello", "world"
        )
        == 1
    )

    assert (
        find_smallest_distance(
            "dog cat hello cat dog dog hello world", "hello", "world"
        )
        == 0
    )
    assert (
        find_smallest_distance("dog cat hello cat dog dog cat world", "hello", "world")
        == 4
    )
