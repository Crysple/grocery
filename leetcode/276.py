class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        dp = [k, 0]#TODO
        # dp[0]: ways of coloring such that c[i] != c[i-1]
        # dp[1]: ways of coloring such that c[i] == c[i-1]
        for _ in range(1, n):
            n_diff_color = sum(dp) * (k - 1)
            n_same_color = dp[0]
            dp = [n_diff_color, n_same_color]
        return sum(dp)
