#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

from queue import Queue

class Node(object):
    def __init__(self, val, level):
        self.val = val
        self.left = None
        self.right = None
        self.level = level
        
    def __str__(self):
        return f"Node(val={self.val}, level={self.level})"
        

def build_tree(indexes):
    # Handle empty indexes
    queue = Queue()
    root = Node(1,1)
    queue.put(root)
    ix = 0
    while True:
        if queue.empty():
            break
        curr = queue.get()
        print (ix, indexes[ix])
        l, r = indexes[ix]
        if l != -1:
            n = Node(l, curr.level + 1)
            curr.left = n
            queue.put(n)
        if r != -1:
            n = Node(r, curr.level + 1)
            curr.right = n
            queue.put(n)
        # Increment the counter
        ix += 1
    return root

def swap_nodes(node, query):
    if node is None:
        return
    if node.level % query == 0:
        node.left, node.right = node.right, node.left        
    swap_nodes(node.left, query)
    swap_nodes(node.right, query)


def in_order(node, path):
    if node is None:
        return
    in_order(node.left, path)
    path.append(node.val)
    in_order(node.right, path)
        
def swapNodes(indexes, queries):
    root = build_tree(indexes)
    x = []
    in_order(root, x)
    ret = []
    for query in queries:
        print("Swap Nodes : ", root.val, root.level, query)
        swap_nodes(root, query)
        path = []
        in_order(root, path)
        ret.append(path)
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
