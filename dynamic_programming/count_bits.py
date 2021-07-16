"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

0 <= n <= 10^5
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        # Time Complexity O(n)
        # Space Complexity O(n)

        # 0 -> 0 0 0 0
        # 1 -> 0 0 0 1
        # 2 -> 0 0 1 0
        # 3 -> 0 0 1 1
        # 4 -> 0 1 0 0
        # 5 -> 0 1 0 1

        # >> 1 shifting by one bit to the right
        dp = [0]

        for i in range(1, n + 1):
            dp.append(dp[i >> 1] + i % 2)

        return dp