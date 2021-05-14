"""
You are given two non-increasing 0-indexed integer arrays nums1 and nums2.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length,

is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length
"""
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        res = i = 0

        for j, b in enumerate(nums2):
            while i < len(nums1) and nums1[i] > b:
                i += 1
            if i == len(nums1): break
            res = max(res, j - i)

        return res

sol = Solution()
print(sol.maxDistance([55,30,5,4,2], [100,20,10,10,5]))