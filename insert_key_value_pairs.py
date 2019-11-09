import argparse
import sys
import os
import avl
import time
import binary_tree as bt
from hash_tables_tacaro import hash_tables as ht
from hash_tables_tacaro import hash_functions as hf


def main():
    tstart = time.time()
    parser = argparse.ArgumentParser(
                description='',
                prog='')

    parser.add_argument('-s',
                        '--struct',
                        type=str,
                        help="Desired Data Structure: hash, AVL, tree",
                        required=True)

    parser.add_argument('-i',
                        '--input_data',
                        type=str,
                        help='Desired dataset to use',
                        required=True)

    parser.add_argument('-b',
                        '--benchmark',
                        type=str,
                        help='Conduct benchmarking? Y/N',
                        required=False)

    args = parser.parse_args()
    data_in = args.input_data
    struct = args.struct

    # create list with all elements, remove duplicates
    file_object = open(data_in, 'r')

    klst = []
    for line in file_object:
        tup = ([int(x) for x in line.split()])
        klst.append(tup)

    if struct == "hash":
        hash_table = ht.LinearProbe(len(klst), hf.h_ascii)
        for tp in klst:
            hash_table.add(tp[0], tp[1])
    if struct == "tree":
        t1 = time.time()
        tree = bt.BinaryTree()
        for tp in klst:
            print(tp)
            tree.insert(k=tp[0], value=tp[1])
        t2 = time.time()
        tree.search(20)
        tree.search(40)
        tree.search(60)
        t3 = time.time()
        tree.search(3.14)
        tree.search(420.69)
        tree.search(999999999999)
        t4 = time.time()

    if args.benchmark == "Y":
        total_time = t4 - tstart
        build_time = t2 - t1
        search_3_items = t3 - t2
        search_3_items_false = t4 - t3
        print("Total run time: " + str(total_time))
        print("Time it took to build struct: " + str(build_time))
        print("Time it took to search for 3 items present in the struct: " +
              str(search_3_items))
        print("Time it took to search for 3 items absent from the struct: " +
              str(search_3_items_false))
    else:
        pass


if __name__ == "__main__":
    main()
