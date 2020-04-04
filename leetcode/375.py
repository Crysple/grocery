class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Bottom up
        dp = [[0] * (n+2) for _ in range(n+2)]
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                dp[j][i] = float('inf')
                for k in range(j, i+1):
                    dp[j][i] = min(dp[j][i], max(dp[j][k-1], dp[k+1][i]) + k)
        return dp[1][n]
    
        # Top down
        @lru_cache(None)
        def _getMoneyAmount(start, end):
            if end - start <= 1:
                return 0
            if end - start == 2:
                return start
            min_cost_money = None
            for i in range(start+1, end):
                cost_money = i + max(_getMoneyAmount(start, i), _getMoneyAmount(i+1, end))
                if min_cost_money:
                    min_cost_money = min(min_cost_money, cost_money)
                else:
                    min_cost_money = cost_money
            return min_cost_money

        return _getMoneyAmount(0, n+1)
