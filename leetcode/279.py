class Solution:
    def numSquares(self, n: int) -> int:
        root = [*range(1, int(n**0.5)+1)]
        squares = [i*i for i in root]
        dp = [0] + [n] * n
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]
