"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        length = len(nums)
        res = list()
        for a in range(length):
            if a > 0 and nums[a] == nums[a - 1]: continue
            for b in range(a + 1, length):
                if b > a + 1 and nums[b] == nums[b - 1]: continue

                c, d = b + 1, length - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                    if total <= target:
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                    if total >= target:
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        return res