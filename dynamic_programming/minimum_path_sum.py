"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if len(grid) == 0 or grid is None:
            return 0

        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dp[i][j] += grid[i][j]

                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                elif i > 0:
                    dp[i][j] += dp[i - 1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[len(grid) - 1][len(grid[0]) - 1]