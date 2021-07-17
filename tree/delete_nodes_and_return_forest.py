"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        # Time Complexity O(n)
        # Space Complexity O(n)
        delete = set(to_delete)
        forest = list()
        if root.val not in delete:
            forest.append(root)

        self.dfs(root, delete, forest)

        return forest

    def dfs(self, root, delete, forest):
        if root is None:
            return None

        root.left = self.dfs(root.left, delete, forest)
        root.right = self.dfs(root.right, delete, forest)

        if root.val in delete:
            if root.left is not None:
                forest.append(root.left)
            if root.right is not None:
                forest.append(root.right)
            return None

        return root