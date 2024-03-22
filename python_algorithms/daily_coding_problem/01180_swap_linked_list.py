"""
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

from typing import Any


class Node:
    def __init__(self, value: Any, nxt: Any = None) -> None:
        self.value = value
        self.nxt = nxt


def swap_pairs(head: Node) -> Node:
    if head is None or head.nxt is None:
        return head

    current = head
    while current and current.nxt:
        if current.value != current.nxt.value:
            current.value, current.nxt.value = current.nxt.value, current.value

        current = current.nxt.nxt

    return head


def print_list(head: Node):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.nxt
    print("")


if __name__ == "__main__":
    _head = Node(1, Node(2, Node(3, Node(4))))
    print_list(swap_pairs(_head))

    _head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print_list(swap_pairs(_head))
