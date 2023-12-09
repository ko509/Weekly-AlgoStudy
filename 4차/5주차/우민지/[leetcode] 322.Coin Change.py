# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] == INF else dp[amount]