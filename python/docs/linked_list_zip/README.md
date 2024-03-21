# Linked List Zip
Write a function called zip lists
Arguments: 2 linked lists
Return: New Linked List, zipped as noted below
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
Try and keep additional space down to O(1)
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


## Whiteboard Process
![Whiteboard](./White%20Board.png)

## Approach & Efficiency

Check for Empty Lists:

Verify if either of the input linked lists (list1 and list2) is empty.
If one list is empty, return the other list as the result.
Initialization:

Initialize two pointers, current1 and current2, to the heads of list1 and list2 respectively.
Zip the Lists:

Iterate through both lists simultaneously (while current1 and current2).
Store the next nodes (next1 and next2) of current1 and current2 respectively.
Link current1's next node to current2 and current2's next node to next1.
Update current1 and current2 to their respective next nodes (next1 and next2).
Handle Unequal Lengths:

If list2 is longer than list1, link the remaining nodes of list2 to the end of list1.
Return Result:

Return the modified list1, which now contains the merged nodes from both input lists.

## Solution

[Link to Code](../../code_challenges/linked_list_zip.py)

# Test the function with the provided examples
Tests location:
[Tests](../../tests/code_challenges/test_linked_list_zip.py)

# Example usage
