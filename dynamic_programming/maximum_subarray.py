"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
"""


class Solution:
    def maxSubArrayKadane(self, nums: list[int]) -> int:
        maximum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            maximum = max(maximum, nums[i])
        return maximum

    def maxSubArrayGreedy(self, nums: list[int]) -> int:
        maximum = current = nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            maximum = max(current, maximum)
        return maximum
