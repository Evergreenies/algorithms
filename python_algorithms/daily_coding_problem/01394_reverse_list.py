"""
Given the head of a singly linked list, reverse it in-place.
"""


class ListNode:
    def __init__(self, value=0, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


def reverse(head: ListNode | None) -> ListNode | None:
    prev, current = None, head
    while current:
        nxt = current.nxt
        current.nxt = prev

        prev = current
        current = nxt

    return prev


def print_list(head: ListNode | None) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.nxt

    print("None")


# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
print_list(head)

reversed_head = reverse(head)
print("Reversed list:")
print_list(reversed_head)
