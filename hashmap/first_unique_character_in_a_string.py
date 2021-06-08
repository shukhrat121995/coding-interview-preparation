"""
Given a string s, return the first non-repeating character in it and return its index.
If it does not exist, return -1.

Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = dict()

        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable[s[i]] = i
            else:
                hashtable[s[i]] = False

        for k, v in hashtable.items():
            if v is not False:
                return v
        return -1