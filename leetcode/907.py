class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # using one stack hinted by discussion
        MOD = 10 ** 9 + 7
        stack = [] # increasing stack (min can block previous array)
        dp = [0] * len(A)
        for i, n in enumerate(A):
            while stack and A[stack[-1]] >= n:
                stack.pop()
            if stack:
                dp[i] = ((i - stack[-1]) * n + dp[stack[-1]]) % MOD
            else:
                dp[i] = (i + 1) * n
            stack.append(i)
        return sum(dp) % MOD
