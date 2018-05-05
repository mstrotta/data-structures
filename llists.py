class LinkedList:
    """ A singly-linked linked list with a single head reference
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        s = ''
        while cur is not None:
            s += '[{}]->'.format(cur.item)
            cur = cur.next
        s += 'NULL'
        return s

    def append(self, val):
        n = Node(val)
        if self.head is None:
            self.head = n
            return

        cur = self.head
        prev = None
        while cur is not None:
            prev = cur
            cur = cur.next

        prev.next = n

    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def insert(self, val, i):
        cnt = 0
        cur = self.head
        prev = None
        while cur is not None and cnt < i:
            prev = cur
            cur = cur.next
            cnt += 1

        n = Node(val)
        n.next = cur
        if prev is None:
            self.head = n
        else:
            prev.next = n
    
    def pop(self, ndx):
        cnt = 0
        cur = self.head
        prev = None
        while cur is not None and cnt < ndx:
            prev = cur
            cur = cur.next
            cnt += 1
        if ndx == cnt and cur is not None:
            if prev is None:
                self.head = self.head.next
                return cur.item
            else:
                prev.next = cur.next
                return cur.item

    def remove(self, val):
        cur = self.head
        prev = None
        while cur is not None:
            if cur.item == val:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next




class Node:
    def __init__(self, val=None):
        self.item = val
        self.next = None

if __name__ == "__main__":
    print('LinkedLists')
    l = LinkedList()
    for i in range(5):
        l.append(i)
    print(repr(l))
    l.insert('i10', 10)
    l.insert('i4', 4)
    l.insert('i0', 0)
    print(l)
    l.reverse()
    print(repr(l))
    l.reverse()
    print(l.pop(0))
    print(l.pop(4))
    print(l.pop(10))
    print(l)
    l.remove('i10')
    print(l)
    l.remove(0)
    l.remove(2)
    print(l)
