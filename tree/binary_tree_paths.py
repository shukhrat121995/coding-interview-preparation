"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePathsIterative(self, root: TreeNode) -> list[str]:
        if root is None:
            return []

        res, stack = [], [(root, "")]

        while stack:
            node, path = stack.pop()
            path += str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
            if node.left is not None:
                stack.append((node.left, path + '->'))
            if node.right is not None:
                stack.append((node.right, path + '->'))

        return res

    def binaryTreePathsRecursive(self, root: TreeNode) -> list[str]:
        paths = list()

        if root is None:
            return paths

        self.dfs(root, "", paths)

        return paths

    def dfs(self, root, path, paths):
        path += str(root.val)
        if root.left is None and root.right is None:
            paths.append(path)
        if root.left is not None:
            self.dfs(root.left, path + '->', paths)
        if root.right is not None:
            self.dfs(root.right, path + '->', paths)
