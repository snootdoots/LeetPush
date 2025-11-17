class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        # recurrence relation = min(f(n-coin1), f(n-coin2))
        for i in range(1, amount+1):
            # e.g. coins = [2, 5]
            # dp = [0, -1, 1, -1, 2, 1]
            for coin in coins:
                if i-coin >= 0: # valid spot
                    if dp[i-coin] != -1:
                        if dp[i] == -1:
                            dp[i] = dp[i-coin] + 1
                        else:
                            dp[i] = min(dp[i], dp[i-coin]+1)
        print(dp)
        return dp[amount]