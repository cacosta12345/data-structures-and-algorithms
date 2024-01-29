class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):

        def traverse(node):
           if node is None:
               return []
           
           my_result = [node.value]
           left_result = traverse(node.left)
           right_result = traverse(node.right)

           return my_result + left_result + right_result
        
        return traverse(self.root)
    
    def in_order(self):
        
        def traverse(node):
           if node is None:
               return []
           
           my_result = [node.value]
           left_result = traverse(node.left)
           right_result = traverse(node.right)

           return left_result + my_result + right_result
        
        return traverse(self.root)
           

    def post_order(self):

        def traverse(node):
           if node is None:
               return []
           
           my_result = [node.value]
           left_result = traverse(node.left)
           right_result = traverse(node.right)

           return left_result + right_result + my_result
        
        return traverse(self.root)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
