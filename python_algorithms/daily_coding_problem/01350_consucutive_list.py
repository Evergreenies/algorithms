"""
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case,
you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""


class Node:
    def __init__(self, value: int = 0, nxt=None) -> None:
        self.value = value
        self.nxt = nxt


def remove_zero_sum_sublist(head: Node) -> Node:
    dummy = Node(0)
    dummy.nxt = head
    cumulative_sum = 0
    sum_map = {0: dummy}

    current = head
    while current:
        cumulative_sum += current.value

        if sum_map.get(cumulative_sum) is not None:
            prev = sum_map[cumulative_sum]
            node = prev.nxt
            temp_sum = cumulative_sum

            while node != current:
                temp_sum += node.value
                del sum_map[temp_sum]
                node = node.nxt

            prev.nxt = current.nxt
        else:
            sum_map[cumulative_sum] = current

        current = current.nxt

    return dummy.nxt


def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.nxt = Node(value)
        current = current.nxt
    return head


# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.nxt else "")
        current = current.nxt
    print()


# Example usage:
values = [3, 4, -7, 5, -6, 6]
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

result_head = remove_zero_sum_sublist(head)
print("Linked List after removing zero-sum sublists:")
print_linked_list(result_head)
