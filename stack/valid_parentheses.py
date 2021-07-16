"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = list()

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif len(stack) == 0 or brackets[stack.pop()] != c:
                return False

        return len(stack) == 0