"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a
total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Input: coins = [1], amount = 1
Output: 1

Input: coins = [1], amount = 2
Output: 2

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Time Complexity O(m*n)
        # Space Complexity O(n)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # coins = [1, 5], amount = 11

        for coin in coins:
            for i in range(coin, amount + 1):
                # dp[1] = min(12, dp[1-1]+1) = 1
                # dp[11] = min(12, dp[11-5]+1) = 3 dp[6] = 2
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1