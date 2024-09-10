"""
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each
tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length
of the longest portion of her path that consists of just two types of apple trees.
"""


def longest_portion_with_two_types(apples):
    # Dictionary to keep track of the frequency of each type of apple in the current window
    fruit_count = {}

    start = 0
    max_length = 0

    for end in range(len(apples)):
        # Add the current apple at 'end' to the dictionary
        if apples[end] in fruit_count:
            fruit_count[apples[end]] += 1
        else:
            fruit_count[apples[end]] = 1

        # If we have more than 2 types of apples, shrink the window from the left
        while len(fruit_count) > 2:
            fruit_count[apples[start]] -= 1
            if fruit_count[apples[start]] == 0:
                del fruit_count[apples[start]]
            start += 1

        # Update the maximum length of the window
        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage:
apples = [2, 1, 2, 3, 3, 1, 3, 5]
print(longest_portion_with_two_types(apples))  # Output: 4
