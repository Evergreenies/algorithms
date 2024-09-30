"""
Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space over time?
"""

import random

from typing import Any


class ListNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.nxt = None


def shuffle_linked_list(head: ListNode | None) -> ListNode | None:
    if not head:
        return None

    # converting tree nodes to list
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.nxt

    # peform Fisher-Yates shuffle on the array of nodes
    length = len(nodes)
    for index in range(length):
        random_idx = random.randint(index, length - 1)
        nodes[index].value, nodes[random_idx].value = (
            nodes[random_idx].value,
            nodes[index].value,
        )

    return head


def print_list(head: ListNode | None) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.nxt

    print("None")


head = ListNode(1)
head.nxt = ListNode(2)
head.nxt.nxt = ListNode(3)
head.nxt.nxt.nxt = ListNode(4)
head.nxt.nxt.nxt.nxt = ListNode(5)

print("Original List:")
print_list(head)

# Shuffle the linked list
shuffled_head = shuffle_linked_list(head)

print("Shuffled List:")
print_list(shuffled_head)
