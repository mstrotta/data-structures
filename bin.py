class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """ Binary Search Tree insertion
        """
        n = Node(val)
        if self.root is None:
            self.root = n
            return

        cur = self.root
        while cur is not None:
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if val < prev.val:
            prev.left = n
        else:
            prev.right = n

    def remove(self, val):
        """ Binary Search Tree deletion
        """
        n = self.search(val)
        # Not in tree
        if n is None:
            return

        # Leaf
        if n.left is None and n.right is None:
            if n.val < n.parent.val:
                n.parent.left = None
            else:
                n.parent.right = None
            return

        # Single subtree
        if n.left is None or n.right is None:
            if n.left is None:
                subtree = n.right
            else:
                subtree = n.left
            if n.val < n.parent.val:
                n.parent.left = subtree
            else:
                n.parent.right = subtree
            return
        # More complicated...



    def contains(self, val):
        return self.search(val) is None

    def search(self, val, root=0):
        """ Binary Search returns the first node that contains val
        """
        if root == 0
            root = self.root
        if root is None:
            return None

        if val < root.val:
            return self.search(val, root.left)
        elif val > root.val:
            return self.search(val, root.right)
        return root
