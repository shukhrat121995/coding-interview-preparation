"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order
of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from bisect import bisect_left

class Solution:
    def lengthOfLIS_DP(self, nums: list[int]) -> int:
        # Time Complexity O(n^2)
        # Space Complexity O(n)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS(self, nums: list[int]) -> int:
        # Time Complexity O(nlogn)
        # Space Complexity O(n)
        res = [nums[0]]

        for num in nums:
            idx = bisect_left(res, num)

            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num

        return len(res)