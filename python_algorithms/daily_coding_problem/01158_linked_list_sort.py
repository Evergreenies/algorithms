"""
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class ListNode:
    def __init__(self, value, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


def get_middle(head: ListNode) -> ListNode:
    if not head:
        return head

    slow, fast = head, head
    while fast.nxt and fast.nxt.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt

    return slow


def merge_sort(head: ListNode) -> ListNode:
    if not head or not head.nxt:
        return head

    # divide list in two parts
    middle = get_middle(head)
    second_half = middle.nxt
    middle.nxt = None

    # sort each half
    left = merge_sort(head)
    right = merge_sort(second_half)

    # merge the sorted parts
    return merge(left, right)


def merge(left: ListNode, right: ListNode) -> ListNode:
    if not left:
        return right

    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.nxt = merge(left.nxt, right)
    else:
        result = right
        result.nxt = merge(left, right.nxt)

    return result


def print_list(head: ListNode) -> None:
    while head:
        print(head.value, end=" -> ")
        head = head.nxt

    print("None")


head = ListNode(4)
head.nxt = ListNode(1)
head.nxt.nxt = ListNode(-3)
head.nxt.nxt.nxt = ListNode(99)

print("Original list:")
print_list(head)

sorted_head = merge_sort(head)

print("Sorted list:")
print_list(sorted_head)
