# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        if ld > rd:
            return ld + 1
        return rd + 1

    def sumMaxLeavesRec(self, root: TreeNode, maxDepth: int) -> int:
        if root is None:
            return 0
        if maxDepth == 1:
            return root.val
        return self.sumMaxLeavesRec(root.left, maxDepth - 1) + self.sumMaxLeavesRec(root.right, maxDepth - 1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        md = self.maxDepth(root)
        return self.sumMaxLeavesRec(root, md)
