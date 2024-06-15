"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""


class ListNode:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.nxt or k == 0:
        return head

    # find the length of linked list
    current, length = head, 1
    while current.nxt:
        current = current.nxt
        length += 1

    # normalize k
    k = k % length
    if k == 0:
        return head

    # find new head and tail
    # make it circular linked list temporarily
    current.nxt = head
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.nxt

    # create new head
    new_head = new_tail.nxt

    # break circular list
    new_tail.nxt = None

    return new_head


def traverse(head: ListNode) -> None:
    while head:
        print(f"{head.value} -> ", end="")
        head = head.nxt

    print("None")


head1 = ListNode(7, ListNode(7, ListNode(3, ListNode(5))))
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original List 1:")
traverse(head1)
rotated1 = rotate_right(head1, 2)
print("Rotated List 1 by 2 places:")
traverse(rotated1)

print("Original List 2:")
traverse(head2)
rotated2 = rotate_right(head2, 3)
print("Rotated List 2 by 3 places:")
traverse(rotated2)
