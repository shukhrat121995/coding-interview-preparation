"""
Given the root of a binary tree, return the sum of all left leaves.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Input: root = [1]
Output: 0

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeavesRecursive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeavesRecursive(root.right)
        return self.sumOfLeftLeavesRecursive(root.left) + self.sumOfLeftLeavesRecursive(root.right)

    def sumOfLeftLeavesIterative(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [root]
        total_sum = 0

        while stack:
            node = stack.pop()
            if node is None:
                continue
            elif node.left and node.left.left is None and node.left.right is None:
                total_sum += node.left.val
                stack.append(node.right)
            else:
                stack.append(node.left)
                stack.append(node.right)

        return total_sum
