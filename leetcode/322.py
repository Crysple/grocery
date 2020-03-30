class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [amount + 1] * (amount + 1)
        ans[0] = 0
        for i in range(min(coins), amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    ans[i] = min(ans[i], ans[i-coin] + 1)
        return ans[-1] if ans[-1] <= amount else -1
