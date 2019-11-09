# Binary Search Tree
[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/trees-tacaro.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/trees-tacaro)
## Introduction
The purpose of this program is to benchmark and compare various data structures in the storage and searching of a series of non-random or random datasets. It utilizes the following files.
- README.md: This file!
- insert_key_value_pairs.py: The main script, contains user argument parsing
- binary_tree.py: A module that implements an unbalanced binary tree
- [Extra Credit Assignment] avl.py: A module that implements a self-balancing AVL-type tree
- binary_tree_tests.py: A testing module for the tree
- kvgen.sh: "Key value generator" bash script that creates test data
- sorted.txt: sorted key value pairs
- rand.txt: random key value pairs
- hash_tables_tacaro: A hash table submodule
- avl_tree: An AVL submodule that aided in development of avl.py
- .gitmodules: submodule tracking


### Benchmarking
Real-time profiling was conducted using the `time` module in python.
*Results: Binary Tree, Unbalanced*
Time it took to build struct: 0.002754688262939453

Time it took to search for 3 items present in the struct: 6.318092346191406e-05

Time it took to search for 3 items absent from the struct: 9.799003601074219e-05

### Installation:
The following builtin python libraries are used:
- os
- sys
- argparse
- random
- time

pycodestyle is required to run the verification tests: `pip install pycodestyle pip install --upgrade pycodestyle pip uninstall pycodestyle`

Future functional testing may involve ssshtest, which can be installed with: `test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest . ssshtest`

Matplotlib is required and can be installed with: `conda activate swe4s conda install matplotlib`
