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