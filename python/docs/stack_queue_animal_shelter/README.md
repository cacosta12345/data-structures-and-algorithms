# Stack and Queue Animal Shelter
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue
Arguments: animal
animal can be either a dog or a cat object.
It must have a species property that is either "cat" or "dog"
It must have a name property that is a string.
dequeue
Arguments: pref
pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![Whiteboard]()

## Approach & Efficiency
Big O considerations:

Time: O(1) -- adding an element to the end of a queue is a constant time operation

Space: O(n) -- space required by the shelter is directly proportional to the number of animals it holds

## Solution
[Link to code](../../code_challenges/stack_queue_animal_shelter.py)