from data_structures.binary_tree import BinaryTree


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def fizz_buzz_tree(root):
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def helper(node):
        if not node:
            return None
        new_node = TreeNode(fizz_buzz(node.value))
        new_node.children = [helper(child) for child in node.children]
        return new_node

    return helper(root)

