"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def generate_subsets(self, index, nums, current, subsets):
        subsets.append(current.copy())
        for i in range(index, len(nums), 1):
            current.append(nums[i])
            self.generate_subsets(i + 1, nums, current, subsets)
            current.pop(-1)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = list()
        self.generate_subsets(0, nums, list(), subsets)
        return subsets