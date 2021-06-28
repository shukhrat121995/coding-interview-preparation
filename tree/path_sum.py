"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf
path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [1,2], targetSum = 0
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSumIterative(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, value = stack.pop()
            if node:
                if node.left is None and node.right is None and node.val == value:
                    return True
                stack.append((node.left, value - node.val))
                stack.append((node.right, value - node.val))

        return False

    def hasPathSumRecursive(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None and targetSum == root.val:
            return True
        else:
            return self.hasPathSumRecursive(root.left, targetSum - root.val) or self.hasPathSumRecursive(root.right,
                                                                                                         targetSum - root.val)
