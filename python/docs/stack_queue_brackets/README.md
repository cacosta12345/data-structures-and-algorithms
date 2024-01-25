# Stack Queue Brackets
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process
![Whiteboard]()

## Approach & Efficiency
Create a dictionary with the different bracket "types" and it's corresponding pair (opening bracket: closing bracket)

Initialize an empty stack

Loop through the characters in the input string and push opening brackets into stack

If a closing bracket is pushed check if the opening bracket was already pushed previously

stack.pop

Big O considerations

Time: O(n) -- scales linearly with the size of the input string

Space: O(n) -- scales linearly with the size of the input string

## Solution

[Link to code](../../code_challenges/stack_queue_brackets.py)