class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def _maxCoins(l, r, ln, rn):
            if l >= r:
                return 0
            if l == r - 1:
                return ln*nums[l]*rn
            ans = 0
            for i in range(l, r):
                lans = _maxCoins(l, i, ln, nums[i])
                rans = _maxCoins(i+1, r, nums[i], rn)
                ans = max(ans, lans+rans+nums[i]*ln*rn)
            return ans
        return _maxCoins(0, len(nums), 1, 1)
