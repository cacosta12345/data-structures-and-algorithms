from data_structures.binary_tree import BinaryTree, Node
from data_structures.hashtable import Hashtable

def tree_intersection(tree_a, tree_b):
    # Helper function to traverse a tree and add its values to a hashtable
    def traverse_and_hash(node, hash_table):
        if node:
            hash_table.set(node.value, True)
            traverse_and_hash(node.left, hash_table)
            traverse_and_hash(node.right, hash_table)

    # Helper function to traverse the second tree and collect values found in the hashtable
    def traverse_and_collect(node, hash_table, result_set):
        if node:
            if hash_table.has(node.value):
                result_set.add(node.value)
            traverse_and_collect(node.left, hash_table, result_set)
            traverse_and_collect(node.right, hash_table, result_set)

    # Initialize a hashtable to store values from the first tree
    hash_table = Hashtable()
    # Initialize a set to store intersecting values
    result_set = set()

    # Fill the hashtable with values from the first tree
    traverse_and_hash(tree_a.root, hash_table)
    # Traverse the second tree and collect values that are also in the first tree
    traverse_and_collect(tree_b.root, hash_table, result_set)

    return list(result_set)


