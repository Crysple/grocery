class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # using one stack hinted by discussion
        MOD = 10 ** 9 + 7
        stack = []
        ans = 0
        for i, n in enumerate(A+[0]):
            while stack and A[stack[-1]] > n:# > or >=
                mid = stack.pop()
                ans += A[mid] * (i-mid) * (mid-(stack[-1] if stack else -1))
                ans %= MOD
            stack += i,
        return ans % MOD
        # First Though O(n)
        # maintaining a monotonically decreasing stack
        # 1, 2, 3, 4, ...
        MOD = 10 ** 9 + 7
        stack = []
        pre_small = []
        # find pre_small --> increasing stack
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                stack.pop()
            pre_small.append(stack[-1] if stack else -1)
            stack.append(i)
        dp = [0] * (len(A) + 1)
        for i in range(len(A)):
            dp[i] = ((i - pre_small[i]) * A[i] + dp[pre_small[i]])%MOD
            
        return sum(dp)%MOD
