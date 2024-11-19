"""
Given an array of integers, find the maximum XOR of any two elements.
"""

INTEGER_32_BIT = 31


class TrieNode:
    def __init__(self) -> None:
        self.left, self.right = None, None


class Trie:
    def insert(self, num: int, root: TrieNode) -> None:
        node = root

        for index in range(INTEGER_32_BIT, -1, -1):
            if not node:
                return

            if ((num >> index) & 1) == 0:
                if not node.left:
                    node.left = TrieNode()

                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()

                node = node.right


def find_maximum_xor(arr: list[int]) -> int:
    root = TrieNode()
    trie = Trie()
    max_xor = 0

    for num in arr:
        trie.insert(num, root)

    for num in arr:
        node = root
        curr_xor = 0

        for index in range(INTEGER_32_BIT, -1, -1):
            if not node:
                continue

            if ((num >> index) & 1) == 0:
                if node.right:
                    curr_xor += 1 << index
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:
                    curr_xor += 1 << index
                    node = node.left
                else:
                    node = node.right

        max_xor = max(max_xor, curr_xor)

    return max_xor


print(find_maximum_xor([3, 10, 5, 25, 2, 8]))
