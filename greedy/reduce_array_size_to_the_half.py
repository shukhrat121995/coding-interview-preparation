"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
"""

from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        res = cur = 0

        for k, v in Counter(arr).most_common():
            res += 1
            cur += v

            if cur >= len(arr) // 2:
                return res