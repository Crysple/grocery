class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m:
            return 0
        MOD = 10 ** 9 + 7
        dp = [[0] * (m+1) for _ in range(n+1)]
        K = k
        for k in range(1, K+1):
            ndp = [[0] * (m+1) for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(k, m+1):
                    if i == 1 and k == 1:
                        ndp[i][j] = 1
                        continue
                    ndp[i][j] = (ndp[i-1][j] * j + sum(dp[i-1][jj] for jj in range(1, j))) % MOD
            dp = ndp
        return sum(dp[n])%MOD
