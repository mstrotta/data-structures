class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        n = Node(val)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            return None

        prev_top = self.top
        self.top = self.top.next
        return prev_top



class Node:
    def __init__(self, val=None):
        self.item = val
        self.next = None
