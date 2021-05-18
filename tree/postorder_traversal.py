# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversalRecursiveSolution(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return self.postorderTraversalRecursiveSolution(root.left) + \
               self.postorderTraversalRecursiveSolution(root.right) + \
               [root.val]

    def postorderTraversalIterativeSolution(self, root:TreeNode) -> list[int]:
        stack = list()
        res = list()
        if root is None:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            if node is not None:
                res.insert(0, node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res

