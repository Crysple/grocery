class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [(s.count('0'), s.count('1')) for s in strs]
        dp = [[[0] * (len(strs)+1) for _ in range(n+1)] for _ in range(m+1)]
        for z in range(m+1):
            for o in range(n+1):
                for i in range(len(strs)):
                    nz, no = z - strs[i][0], o - strs[i][1]
                    if nz >= 0 and no >= 0:
                        dp[z][o][i+1] = max(dp[nz][no][i] + 1, dp[z][o][i])
                    else:
                        dp[z][o][i+1] = dp[z][o][i]
        return dp[-1][-1][-1]
