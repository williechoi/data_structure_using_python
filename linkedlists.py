class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first node to second node
list1.head.next = e2

# Link second node to third node
e2.next = e3

list1.print_all()
