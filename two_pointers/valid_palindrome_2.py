"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""


class Solution:
    def isPalindrome(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return self.isPalindrome(s, start + 1, end) or self.isPalindrome(s, start, end - 1)
            start += 1
            end -= 1

        return True