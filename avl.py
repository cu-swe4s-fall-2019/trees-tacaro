class Node(object):
    """The basis of the AVL tree is the node object"""

    def __init__(self, key=None):
        """Instantiates a Node object
        key: the key of the node
        value: the value of the node
        parent: the parent node. None if root.
        left: the left child of the Node
        right: the right child of the Node
        """
        self.key = key
        self.value = None
        self.parent = None
        self.left = None
        self.right = None

        def search(self, key):
            """Finds and returns the value from node containing key
            key: the desired key we want the corresponding value
            Returns: value of node with key"""
            if key == self.key:
                return self.value
            elif key < self.key:
                return self.left.search(key)
            elif key > self.key:
                return self.right.search(key)
            else:
                raise ValueError("Node not found!")

        def insert(self, node):
            if node.key < self.key:
                if self.left is None:
                    node.parent = self
                    self.left = node
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    node.parent = self
                    self.right = node
                else:
                    self.right.insert(node)

            def height(node):
                if node is None:
                    return -1
                else:
                    return node.height

            def update_height(node):
                node.height = max(height(node.left), height(node.right)) + 1

class AVL(object):

    def __init__(self):
        self.root = None

    def find_min(self):
        return self.root and self.root.find_min()

    def next_larger(self, key):
        node = self.find(k)
        return node and node.next_larger()

        def left_rotate(self, x):
            y = x.right
            y.parent = x.parent
            if y.parent is None:
                self.root = y
            else:
                if y.parent.left is x:
                    y.parent.left = y
                elif y.parent.right is x:
                    y.parent.right = y
            x.right = y.left
            if x.right is not None:
                x.right.parent = x
            y.left = x
            x.parent = y
            update_height(x)
            update_height(y)

        def right_rotate(self, x):
            y = x.left
            y.parent = x.parent
            if y.parent is None:
                self.root = y
            else:
                if y.parent.left is x:
                    y.parent.left = y
                elif y.parent.right is x:
                    y.parent.right = y
            x.left = y.right
            if x.left is not None:
                x.left.parent = x
            y.right = x
            x.parent = y
            update_height(x)
            update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node to be inserted.
        """
        node = AVLNode(None, k)
        if self.root is None:
            # The root's parent is None.
            self.root = node
        else:
            self.root.insert(node)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = AVLNode(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
        else:
            deleted = node.delete()
        self.rebalance(deleted.parent)
