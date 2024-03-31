"""
Given a singly linked list and an integer k, remove the kth last element from 
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node:
    def __init__(self, value: int = 0, nxt=None):
        self.value = value
        self.nxt = nxt


def remove_nth_from_end(head, kth: int) -> Node:
    fast = head
    slow = head
    for _ in range(kth):
        if not fast:
            return head.nxt

        fast = fast.nxt

    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt

    slow.nxt = slow.nxt.nxt

    return head


def print_list(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.nxt

    print("None")


if __name__ == "__main__":
    _head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = remove_nth_from_end(_head, 2)
    print_list(result)

    _head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = remove_nth_from_end(_head, 4)
    print_list(result)
