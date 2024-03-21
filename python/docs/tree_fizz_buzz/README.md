# Tree Fizz Buzz


## Whiteboard Process
![whiteboard](./White%20Board.png)

## Approach & Efficiency
Define Helper Functions:

Define a helper function fizz_buzz that takes a value as input and returns "Fizz" if the value is divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, or the string representation of the value otherwise.
Traverse the Tree Recursively:

Implement a recursive helper function helper that traverses the original k-ary tree.
For each node in the tree:
Apply the fizz_buzz function to the node's value to determine the modified value.
Create a new node with the modified value.
Recursively call the helper function for each child of the current node.
Assign the list of modified children to the new node.
Return the root of the new tree.
Invoke the Helper Function:

Invoke the helper function with the root of the original k-ary tree as input.
Return the root of the new tree.

## Solution

[Link to Code](../../code_challenges/tree_fizz_buzz.py)

# Example usage

