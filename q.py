class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        n = Node(val)
        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self):
        if self.head is None:
            return None
        prev_head = self.head
        self.head = self.head.next
        return prev_head

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
