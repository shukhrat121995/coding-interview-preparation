"""
You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its
concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.
"""

# Naive Solution

"""
class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if len(set(s[:i])) == len(set(s[i:])):
                res += 1
        return res
"""

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        res = 0
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                res += 1
        return res
