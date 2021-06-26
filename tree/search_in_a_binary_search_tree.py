"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search_iterative(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root

        stack = [root]
        while stack:
            temp = stack.pop()
            if temp and val < temp.val:
                stack.append(temp.left)
            elif temp and val > temp.val:
                stack.append(temp.right)
            else:
                return temp

    def search_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if root and val < root.val:
            return self.search_recursive(root.left, val)
        elif root and val > root.val:
            return self.search_recursive(root.right, val)
        return root

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.search_iterative(root, val)
