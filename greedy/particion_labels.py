"""
You are given a string s. We want to partition the string into as many parts as possible so that
each letter appears in at most one part.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]

1 <= s.length <= 500
s consists of lowercase English letters.
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        left, right = 0, 0
        res = list()
        last_index = {c: i for i, c in enumerate(s)}

        for i in range(len(s)):
            right = max(right, last_index[s[i]])

            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res