"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0: return False
            if target == 0: return True
            if target in cache: return False
            cache.add(target)
            for i, e in enumerate(nums):
                if dfs(nums[i + 1:], target - e, cache): return True
            return False

        s = sum(nums)
        if s % 2 != 0: return False
        return dfs(nums, s // 2, set())