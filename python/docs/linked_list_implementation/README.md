# Linked List Implementation
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
    Arguments: value
    Returns: nothing
    Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
    Arguments: value
    Returns: Boolean
    Indicates whether that value exists as a Node’s value somewhere within the list.
to string
    Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"


## Whiteboard Process
![Whiteboard](./linkedlist.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I followed along with JB's lecture and wrote the same code. 


## Solution

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        current = self.head
        string_representation = ""

        while current:
            formatted_current_value = f"{{  {current.value}  }} ->"
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"

        return string_representation


# Test the function with the provided examples


# Example usage
