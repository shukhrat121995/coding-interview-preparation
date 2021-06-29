"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        visible_nodes = list()
        if root is None:
            return visible_nodes

        stack = [root]

        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                if i == size - 1:
                    visible_nodes.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        return visible_nodes