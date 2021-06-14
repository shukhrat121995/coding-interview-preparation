# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        # Time Complexity O(n)
        # Space Complexity O(n)

        total = 0
        if root is None:
            return total

        stack = [root]

        while stack:
            temp = stack.pop()

            if low <= temp.val <= high:
                total += temp.val
            if temp.left is not None and temp.val > low:
                stack.append(temp.left)
            if temp.right is not None and temp.val < high:
                stack.append(temp.right)

        return total