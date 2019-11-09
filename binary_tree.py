class Node:
    '''
    key: an item representing the storage key: int, str
    value: the item represented by the key: str, int, float, list, etc.
    left: an object of class Node. Represents left child of Node.
    right: an object of class Node. Represents right child of Node.
    '''
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, keys=None, values=None):
        self.root = None

    def insert(self, k, value=None):
        '''
        key: an item representing the storage key: int, str
        value: the item represented by the key: str, int, float, list, etc.
        '''
        if self.root is None:
            self.root = Node(k, value)
        else:
            self.branch(k, value, self.root)

    def branch(self, key, value, node):
        """Branching of tree"""
        if key < node.key:
            if node.left is not None:
                self.branch(key, value, node.left)
            else:
                node.left = Node(key, value)
        else:
            if node.right is not None:
                self.branch(key, value, node.right)
            else:
                node.right = Node(key, value)

    def search(self, key):
        '''
        self: an object of class Node: class
        key: a key whose corresponding value you wish to return: int, str
        '''
        if self.root is None:
            return -1
        else:
            return self.locate(key, self.root)

    def locate(self, k, node):
        """Locates correct branch --> correct node, based on k"""
        if k == node.key:
            return node
        elif node.right is None and node.left is None:
            return None
            print("k not found!")
        elif k < node.key and node.left is not None:
            return self.locate(k, node.left)
        elif k > node.key and node.right is not None:
            return self.locate(k, node.right)
