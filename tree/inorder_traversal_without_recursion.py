"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
without recursion
"""

# Inorder Traversal Left, Root, Right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    current = root
    stack = list()
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val)
            current = current.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inorderTraversal(root)