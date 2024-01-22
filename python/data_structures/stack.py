from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
