import unnitest
import random
import os
import sys


class Test_Binary_Tree(unittest.TestCase):
    """Tests for Binary Search Tree"""

    def test_hist_already_exists(self):
        with self.assertRaises(OSError):
            dv.histogram([1, 2, 3, 4], 'already.png')

    def test_mean_mixed_list(self):
        self.assertEqual(ml.list_mean(['a', 2, 'c', '4']), 3)
