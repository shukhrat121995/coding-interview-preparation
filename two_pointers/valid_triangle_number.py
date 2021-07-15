"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them
as side lengths of a triangle.

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Input: nums = [4,2,3,4]
Output: 4

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        # Time Complexity O(n^2)
        # Space Complexity O(1)
        nums.sort()
        counter = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                a = nums[l]
                b = nums[r]
                c = nums[i]
                if a + b > c:
                    counter += r - l
                    r -= 1
                else:
                    l += 1

        return counter