"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = list()

        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])

        return res
