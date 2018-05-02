class LinkedList:
    """ A singly-linked linked list with a single head reference
    """
    def __init__(self):
        self.head = None

    def append(self, val):
        n = Node(val)
        if self.head is None:
            self.head = n
            return

        cur = self.head
        prev = None
        while cur is not None:
            cur = cur.next

        prev.next = n

class Node:
    def __init__(self, val=None):
        self.item = val
        self.next = None
