class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # O(KlogN) another DP formula
        dp = [0] * (K+1)
        for n in range(1, N+1):
            for k in range(K, 0, -1):
                dp[k] += dp[k-1] + 1
                if dp[k] >= N:
                    return n

        # O(KN) Bottom up with monotonicity optimization
        dp = [*range(N+1)]
        for egg in range(2, K+1):
            f0 = 1
            ndp = [0]
            for curf in range(1, N+1):
                while f0 <= curf and dp[f0-1] < ndp[curf-f0]:
                    f0 += 1
                ndp.append(1 + min(dp[f0-1], ndp[curf-f0+1] if f0>1 else N))
            dp = ndp
        return dp[-1]

        # O(KNlogN) Recursive with bs optimization
        @lru_cache(None)
        def dfs(curf, egg):
            if curf == 0:
                return 0
            if egg == 0:
                return N
            if egg == 1:
                return curf
            if egg > math.log2(curf) + 1:
                return int(math.log2(curf)) + 1
            lo, hi = 1, curf
            while lo < hi:
                mid = (lo + hi) // 2
                if dfs(mid-1, egg-1) < dfs(curf-mid, egg):
                    lo = mid + 1
                else:
                    hi = mid
            return 1 + min(dfs(lo-1, egg-1), dfs(curf-lo+1, egg) if lo-1>0 else N)
        return dfs(N, K)

