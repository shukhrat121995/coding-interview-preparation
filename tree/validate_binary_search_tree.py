# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, left=None, right=None) -> bool:
        if root is None:
            return True

        if left is not None and left.val >= root.val:
            return False

        if right is not None and right.val <= root.val:
            return False

        return self.isValidBST(root.left, left, root) and self.isValidBST(root.right, root, right)