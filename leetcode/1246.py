class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        
        # inspired by discussion
        dp = collections.defaultdict(lambda: 0)
        dp.update({(i, i):1 for i in range(n)})
        for hi in range(1, n):
            for lo in range(hi-1, -1, -1):
                dp[lo, hi] = min(dp[lo, k] + dp[k+1, hi] for k in range(lo, hi))
                if arr[lo] == arr[hi]:
                    dp[lo, hi] = min(dp[lo, hi], max(1, dp[lo+1, hi-1]))
                #dp[lo, hi] = min([min(dp[lo+1, hi], dp[lo, hi-1]) + 1] + [dp[lo, k-1]+max(1, dp[k+1, hi-1]) for k in range(lo, hi) if arr[k] == arr[hi]])
        return dp[0, n-1]
        # 1 3 3 4 4 1
        # 简单的想法就是把整个串分成两半做区间dp，这样是O(n^3)，即
        # dp[i, j] = dp[i, k]+dp[k+1, j] for k in [i, j-1]
        # 但是这个公式处理不了需要中间先消除，然后两边可以合并成一个Palindrome的情况
        # 考虑首尾长度为一的情形， if arr[j] == arr[i]，then dp[i, j] = max(1, dp[i+1, j-1])
        # Generally, if a[i:i+l] == a[j-l+1:j+1][::-1], then dp[i, j] = max(1, dp[i+l, j-l])
        
        dp = {(i, i):1 for i in range(n)}
        for hi in range(1, n):
            for lo in range(hi-1, -1, -1):
                dp[lo, hi]  = float('inf')
                for k in range(lo, hi):
                    dp[lo, hi] = min(dp[lo, hi], dp[lo, k] + dp[k+1, hi])
                offset = 0
                while hi-offset >= lo+offset and arr[hi-offset] == arr[lo+offset]:
                    offset += 1
                if offset:
                    dp[lo, hi] = min(dp[lo, hi], max(1, dp.get((lo+offset, hi-offset), 0)))
        #print(dp)
        return dp[0, n-1]
