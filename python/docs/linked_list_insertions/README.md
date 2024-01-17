# Linked List Insertions
Write the following methods for the Linked List class:

append
    arguments: new value
    adds a new node with the given value to the end of the list

insert before
    arguments: value, new value
    adds a new node with the given new value immediately before the first node that has the value specified

insert after
    arguments: value, new value
    adds a new node with the given new value immediately after the first node that has the value specified


## Whiteboard Process
![Whiteboard](./linkedlistinsertions.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
For Append, check !current.head and make a new node since if there is no current.head that means the list is either empty or it went through all of them already and make a new node
For insert before, check if self.head.value = target, then insert new node
For insert after, check if current.value != target, then insert new node

Big O considerations:
Time: O(n) -- worst case scenario is we have to traverse the entire list 
Space: O(1) -- The space complexity remains constant because only one new node is created, irrespective of the size of the list.


## Solution

def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        if self.head is None:
            raise TargetError("List is empty")
        if self.head.value == target:
            self.insert(value)
            return
        current = self.head
        while current.next and current.next.value != target:
            current = current.next
        if current.next is None:
            raise TargetError(f"Target {target} not found in the list")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def insert_after(self, target, value):
        current = self.head
        while current and current.value != target:
            current = current.next
        if current is None:
            raise TargetError(f"Target {target} not found in the list")
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        


class TargetError(Exception):
    pass

# Test the function with the provided examples


# Example usage

Append

Initial List
Method Args
Resulting List

head -> {1} -> {3} -> {2} -> X
Arg =5
head -> {1} -> {3} -> {2} -> {5} -> X

head -> X
Arg=1
head -> {1} -> X

Insert Before

Initial List
Method Args
Resulting List

head -> {1} -> {3} -> {2} -> X
Args= 3, 5
head -> {1} -> {5} -> {3} -> {2} -> X

head -> {1} -> {3} -> {2} -> X
Args = 1, 5
head -> {5} -> {1} -> {3} -> {2} -> X

head -> {1} -> {2} -> {2} -> X
Args = 2, 5
head -> {1} -> {5} -> {2} -> {2} -> X

head -> {1} -> {3} -> {2} -> X
Args= 4, 5
No change, method exception

Insert After

Initial List
Method Args
Resulting List

head -> {1} -> {3} -> {2} -> X
Args = 3, 5
head -> {1} -> {3} -> {5} -> {2} -> X

head -> {1} -> {3} -> {2} -> X
Args = 2, 5
head -> {1} -> {3} -> {2} -> {5} -> X

head -> {1} -> {2} -> {2} -> X
Args = 2, 5
head -> {1} -> {2} -> {5} -> {2} -> X

head -> {1} -> {3} -> {2} -> X
Args = 4, 5
No change, method exception