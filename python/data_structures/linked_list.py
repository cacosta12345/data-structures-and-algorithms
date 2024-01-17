class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    

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
            formatted_current_value = f"{{ {current.value} }} -> "
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"

        return string_representation
    
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

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k cannot be negative")
        
        lead, follow = self.head, self.head

        for _ in range(k):
            if lead is None:
                raise TargetError("k is larger than the list length")
            lead = lead.next

        while lead and lead.next:
            lead = lead.next
            follow = follow.next

        if follow is None or (k > 0 and lead is None):
            raise TargetError("List is shorter than k elements")
        
        return follow.value


class TargetError(Exception):
    pass
