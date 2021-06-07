"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # Time Complexity O(n)
        # Space Complexity O(n)

        # create a list of English vowels
        vowels = {'a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U'}

        # create a list of characters
        characters = list(s)

        # pointers
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and characters[start] not in vowels:
                start += 1

            while start < end and characters[end] not in vowels:
                end -= 1

            # swap letters
            characters[start], characters[end] = characters[end], characters[start]

            start += 1
            end -= 1

        return "".join(characters)