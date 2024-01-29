from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        
        node = Node(value)

        if self.root is None:
            self.root = node
        
        def traverse(node, node_to_add):
            if node is None: 
                return

            if node_to_add.value < node.value:
                if node.left is None:
                    node.left = node_to_add
                else:
                    traverse(node.left, node_to_add)

            elif node_to_add.value > node.value:
                if node.right is None:
                    node.right = node_to_add
                else: 
                    traverse(node.right, node_to_add)

        traverse(self.root, node)
        
    
    def contains(self, value):
  
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
