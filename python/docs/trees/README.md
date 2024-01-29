# Binary Tree and BST Implementation

Features
Node
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order
Each depth first traversal method should return an array of values, ordered appropriately.
Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process
![Whiteboard]()

## Approach & Efficiency

* Create a binary tree class with the 3 main methods, pre_order, in-order, post-order

* Implement a binary search tree using the binary_tree class and node previously defined

* Add methods add and contains

Big O considerations:
    Binary_tree.py: 
        Time: O(n) -- linear to amount of nodes
        Space: O(h) -- where h is the height of the tree

    Binary_Search_tree.py:
        Time: O(n) -- worst case where nodes are unbalanced. O(log n) if balanced
        Space: O(n) -- worst case where nodes are unbalanced. O(log n) if balanced


## Solution

[Link to code](../../data_structures/binary_tree.py)