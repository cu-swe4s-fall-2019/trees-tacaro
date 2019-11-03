class Node:
    '''
    key: an item representing the storage key: int, str
    value: the item represented by the key: str, int, float, list, etc.
    left: an object of class Node. Represents left child of Node.
    right: an object of class Node. Represents right child of Node.
    '''
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value):
    '''
    root: an object of class Node: class
    key: an item representing the storage key: int, str
    value: the item represented by the key: str, int, float, list, etc.
    '''
    if root.key is None:
        root.key = key
        root.value = value
    elif key > root.key:
        insert(root.right, key, value)
    elif key < root.key:
        insert(root.left, key, value)
    else:
        return -1


def search(root, key):
    '''
    root: an object of class Node: class
    key: a key whose corresponding value you wish to return: int, str
    '''
    if root.key is None:
        raise ValueError("Root key is None")
    if root.key == key:
        return root.value
    elif key < root.key:
        search(root.left, key)
    elif key > root.key:
        search(root.right, key)
    else:
        return -1
