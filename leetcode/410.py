class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Bottom up with optimization (utilizing monotonicity) O(n^2) AC
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1]+i)
        for i in range(N):
            for j in range(i+1):
                dp[j][i] = prefix_sum[i+1] - prefix_sum[j]
        for cm in range(1, m):
            for i in range(N):
                nsum, k0 = 0, -1
                for j in range(i):
                    if j > 0:
                        nsum -= nums[j-1]
                    while k0 <= i-cm and nsum < dp[k0+1][i]:
                            nsum += nums[k0+1]
                            k0 += 1
                    if k0 == i-cm+1:
                        dp[j][i] = dp[k0][i]
                    else:
                        dp[j][i] = min(nsum, dp[k0][i])
        return dp[0][N-1]

        # Top down without optimization O(n^3) failed
        @lru_cache(None)
        def _splitArray(start, end, m, largest_sum):
            if m == 1:
                return sum(nums[start:end])
            cul_sum = 0
            for i in range(start, end-1):
                cul_sum += nums[i]
                if cul_sum > largest_sum:
                    break
                rest = _splitArray(i+1, end, m-1, largest_sum)
                largest_sum = min(largest_sum, max(cul_sum, rest))
            return largest_sum
        
        return _splitArray(0, len(nums), m, float('inf'))
