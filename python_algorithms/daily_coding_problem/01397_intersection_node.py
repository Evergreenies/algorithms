"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class ListNode:
    def __init__(self, value=0, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


def get_length(head: ListNode | None) -> int:
    length, current = 0, head
    while current:
        length += 1
        current = current.nxt

    return length


def get_intersection_node(
    head_a: ListNode | None, head_b: ListNode | None
) -> ListNode | None:
    length_a = get_length(head_a)
    length_b = get_length(head_b)

    current_a, current_b = head_a, head_b
    if length_a > length_b:
        for _ in range(length_a - length_b):
            if current_a:
                current_a = current_a.nxt
    else:
        for _ in range(length_b - length_a):
            if current_b:
                current_b = current_b.nxt

    while current_a and current_b:
        if current_a == current_b:
            return current_a

        current_a = current_a.nxt
        current_b = current_b.nxt

    return None


def print_list(head: ListNode | None) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.nxt

    print("None")


# Example usage
# Creating two intersecting linked lists
# A = 3 -> 7 -> 8 -> 10
# B = 99 -> 1 -> 8 -> 10
node8 = ListNode(8, ListNode(10))
headA = ListNode(3, ListNode(7, node8))
headB = ListNode(99, ListNode(1, node8))

intersection = get_intersection_node(headA, headB)
if intersection:
    print(f"Intersection at node with value: {intersection.value}")
else:
    print("No intersection")
