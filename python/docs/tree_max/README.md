# Tree Max

Write the following method for the Binary Tree class

find maximum value
Arguments: none
Returns: number


## Whiteboard Process
![whiteboard]()

## Approach & Efficiency

Set default value for max to negative inf.

Traverse the binary tree and check if the current value is greater than max and updating if true

Return max value

Big O:
    Time: O(n) -- linear to amount of nodes
    
    Space: O(n) -- linear to number of nodes

## Solution

[Link to Code](../../data_structures/binary_tree.py)

# Example usage
Tree: [2, 7,5,2,6,9,5,11,4]
Return: 11
