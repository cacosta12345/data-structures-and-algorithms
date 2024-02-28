# Tree Intersection
Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process
![Whiteboard]()

## Approach & Efficiency
The solution to the "Tree Intersection" challenge involves a two-step process:

Traverse Both Trees: The algorithm begins by traversing both binary trees. This traversal can be done using any standard tree traversal method (e.g., pre-order, in-order, or post-order). The goal of this traversal is to visit each node in the trees.

Hash Table for Intersection Detection: As we traverse the first tree, we store each encountered value in a hash table. Then, as we traverse the second tree, we check each value against the hash table. If a value from the second tree is found in the hash table, it means this value exists in both trees, and therefore, it's added to the result set.

This method ensures that we efficiently identify all values present in both binary trees by leveraging the hash table's quick lookup capabilities to check for intersections.

Big O:
    Time: O(n + m)
    Space: O(n)

## Solution

[Link to Code](../../code_challenges/tree_intersection.py)



# Test the function with the provided examples
Input:
                 150           
               /        \         
        100                250    
      /     \             /   \   
   75         160      200     350
 /    \     /     \               
125  175   300   500      

                 42           
             /       \         
        100             600    
      /    \           /   \   
   15       160     200     350
 /    \    /    \              
125  175   4   500      

Output: [100,160,125,175,200,350,500]


# Example usage
