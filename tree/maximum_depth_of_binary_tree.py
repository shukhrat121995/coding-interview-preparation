# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.maxDepthRecursive(root.left)
        right = self.maxDepthRecursive(root.right)

        return max(left, right) + 1

    def maxDepthIterative(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])

        return max_depth