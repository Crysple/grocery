class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # Optimized version with stack: O(n)
        stack = []
        ans = 0
        for n in arr:
            while stack and stack[-1] <= n:
                ans += stack.pop() * min(stack[-1:] + [n])
            stack.append(n)
        while len(stack) > 1:
            ans += stack.pop() * stack[-1]
        return ans


        # V2: See the discussion, get the intuitive: O(n^2)
        # cost = 0
        # while len(arr) > 1:
        #     i = arr.index(min(arr))
        #     cost += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)
        # return cost
        
        # V1: First Thought dp: O(n^3)
        # dp = dict()
        # def _mctFromLeafValues(l, r):
        #     """Return ans and max"""
        #     if r - l == 1:
        #         return 0, arr[l]
        #     if r - l == 2:
        #         return arr[l] * arr[l + 1], max(arr[l:r])
        #     if (l, r) in dp:
        #         return dp[l, r]
        #     dp[l, r] = [-1, 0]
        #     for i in range(l+1, r):
        #         lans, lm = _mctFromLeafValues(l, i)
        #         rans, rm = _mctFromLeafValues(i, r)
        #         root = lans + rans + lm * rm
        #         # if (l,r) == (0,3):
        #         #     print((l, i), (i, r), lans, rans, root)
        #         if dp[l, r][0] == -1 or root < dp[l, r][0]:
        #             dp[l, r][0] = root
        #             dp[l, r][1] = max(lm, rm)
        #     return dp[l, r]
        # return _mctFromLeafValues(0, len(arr))[0]
            
