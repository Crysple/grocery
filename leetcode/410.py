class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary Search solution after seeing the solution
        l, r = max(nums), sum(nums) + 1
        while l < r:
            mid = l + (r - l) // 2
            csum = cnt = 0
            for n in nums:
                csum += n
                if csum > mid:
                    csum = n
                    cnt += 1
            if cnt + 1 > m: # mid is still too small
                l = mid + 1
            else:
                r = mid
        return l
        # DP solution after seeing the solution
        dp = nums[:1]
        for n in nums[1:]:
            dp.append(n + dp[-1])
        tdp = [float('inf')] * len(nums)
        for cm in range(1, m):
            for i in range(len(nums)):
                n_sum = 0
                for j in range(i, cm-1, -1):
                    n_sum += nums[j]
                    tdp[i] = min(tdp[i], max(n_sum, dp[j-1]))
            dp = tdp
            tdp = [float('inf')] * len(nums)
        return dp[-1]
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
