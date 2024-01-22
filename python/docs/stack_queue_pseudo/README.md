# Stack and Queue Psuedo
Create a new class called pseudo queue.
Do not use an existing Queue.
Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue
Methods:
enqueue
Arguments: value
Inserts a value into the PseudoQueue, using a first-in, first-out approach.
dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.
NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.


## Whiteboard Process
![Whiteboard]()

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O Considerations: 

Time: O(n) -- If stack2 is empty, all elements from stack1 are popped and pushed onto stack2.

Space: O(n) -- In the worst case, all elements might be stored in both stacks during the transfer process


## Solution

[Link to Code](../../code_challenges/stack_queue_pseudo.py)


# Test the function with the provided examples


# Example usage
