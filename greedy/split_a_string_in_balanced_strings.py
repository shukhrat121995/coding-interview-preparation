"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Time Complexity O(n)
        # Space Complexity O(1)
        res = 0
        count = 0

        for c in s:
            if c == 'L':
                count -= 1
            else:
                count += 1

            if count == 0:
                res += 1

        return res