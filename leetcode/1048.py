class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {w: 1 for w in words}
        ans = 1
        for w in sorted(words, key=len)[1:]:
            for i in range(len(w)):
                dp[w] = max(dp[w], dp.get(w[:i]+w[i+1:], 0)+1)
            ans = max(ans, dp[w])
        return ans
