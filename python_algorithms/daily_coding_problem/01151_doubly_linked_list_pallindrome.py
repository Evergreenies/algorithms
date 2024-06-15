"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class DoublyListNode:
    def __init__(self, value, prev=None, nxt=None) -> None:
        self.value = value
        self.prev = prev
        self.nxt = nxt


def is_pallindrome_doubly(head: DoublyListNode) -> bool:
    if not head:
        return True

    # find the tail
    tail = head
    while tail.nxt:
        tail = tail.nxt

    # compare both ends
    while head != tail and head.prev != tail:
        if head.value != tail.value:
            return False

        head = head.nxt
        tail = tail.prev

    return True


if __name__ == "__main__":
    node1 = DoublyListNode(1)
    node2 = DoublyListNode(4, node1)
    node3 = DoublyListNode(3, node2)
    node4 = DoublyListNode(4, node3)
    node5 = DoublyListNode(1, node4)
    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node5

    assert is_pallindrome_doubly(node1) is True
