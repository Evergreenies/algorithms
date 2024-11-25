"""
Given the head to a singly linked list, where each node also has a “random” pointer that points to 
anywhere in the linked list, deep clone the list.
"""


class Node(object):
    def __init__(self, value: int, nxt=None, random=None) -> None:
        self.value = value
        self.nxt = nxt
        self.random = random

def copy_random_list(head: Node) -> Node | None:
    if not head:
        return head

    # create new copy of each node and placed it exactly next to the original node
    current = head
    while current:
        new_node = Node(current.value, current.nxt)
        current.nxt = new_node
        current = new_node.nxt

    # assign random pointers for each copied nodes
    current = head
    while current:
        if current.random:
            current.nxt.random = current.random.nxt 

        current = current.nxt.nxt

    # restore original list and separate copied list
    original = head 
    copy = head.nxt
    copy_head = copy
    while original:
        original.nxt = original.nxt.nxt
        if copy.nxt:
            copy.nxt = copy.nxt.nxt

        original = original.nxt
        copy = copy.nxt

    return copy_head

def print_list(head: Node | None):
    while head:
        print(f"Value: {head.value}, Random: {head.random.value if head.random else None} -> ", end="")
        head = head.nxt

    print("None")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.nxt = node2
node2.nxt = node3
node1.random = node3
node2.random = node1
node3.random = node2

print_list(node1)
print_list(copy_random_list(node1))

