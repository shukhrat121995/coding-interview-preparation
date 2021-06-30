"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node
never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9]

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convert(self, nums: list[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, left, mid - 1)
        root.right = self.convert(nums, mid + 1, right)
        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if nums is None or len(nums) <= 0:
            return None
        return self.convert(nums, 0, len(nums) - 1)
