from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue

def breadth_first(tree):
    if tree.root is None:
        return []
    
    queue = Queue()
    queue.enqueue(tree.root)
    result = []
    while not queue.is_empty():
        current_node = queue.dequeue()
        result.append(current_node.value)
        if current_node.left:
            queue.enqueue(current_node.left)
        if current_node.right:
            queue.enqueue(current_node.right)
            
    return result
