import unittest
import random
import os
import sys
import binary_tree as bt


class Test_Binary_Tree(unittest.TestCase):
    """Tests Binary Search Tree"""

    def search_null_node(self):
        A = bt.Node()
        with self.assertRaises(ValueError):
            search(A, 1)

    def insert_value(self):
        A = bt.Node()
        bt.insert(A, 1, 'one')
        self.assertEqual(A.key, 'one')


if __name__ == '__main__':
    unittest.main()
