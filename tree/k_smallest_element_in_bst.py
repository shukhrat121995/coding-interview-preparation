class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Time Complexity O(n)
        # Space Complexity O(n)
        nums = [0, None]

        def inorder(root, k):
            if root is None:
                return
            inorder(root.left, k)
            nums[0] += 1
            if k == nums[0]:
                nums[1] = root.val
                return
            inorder(root.righ, k)

        inorder(root, k)
        return nums[1]

