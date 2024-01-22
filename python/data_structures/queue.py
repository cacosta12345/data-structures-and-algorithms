from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value
