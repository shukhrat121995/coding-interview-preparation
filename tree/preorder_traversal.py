# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalRecursiveSolution(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversalRecursiveSolution(root.left) + \
               self.preorderTraversalRecursiveSolution(root.right)

    def preorderTraversalIterativeSolution(self, root:TreeNode) -> list[int]:
        stack = list()
        res = list()
        if root is None:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res