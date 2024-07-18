"""
Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form.

For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
"""


class Node:
    def __init__(self, value=0, nxt=None):
        self.value = value
        self.nxt = nxt


def rearrange_low_high(head: Node) -> Node:
    if not head or not head.nxt:
        return head

    low_head = head
    low_tail = head
    high_head = head.nxt
    high_tail = head.nxt

    while high_tail:
        low_tail.nxt = high_tail.nxt
        low_tail = low_tail.nxt

        high_tail.nxt = low_tail.nxt
        high_tail = high_tail.nxt

    low_tail.nxt = high_head

    return low_head


_head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

rearrange_head = rearrange_low_high(_head)

while rearrange_head:
    print(rearrange_head.value, end=" -> ")
    rearrange_head = rearrange_head.nxt

print("None")
