class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        prefix_sum = [0]
        for n in nums:
            prefix_sum += (prefix_sum[-1]+n),
        @lru_cache(None)
        def PredictTheWinner(i, j):
            if i == j:
                return nums[i]
            return prefix_sum[j+1] - prefix_sum[i] - min(PredictTheWinner(i+1, j), PredictTheWinner(i, j-1))
        return PredictTheWinner(0, len(nums)-1) >= prefix_sum[-1]/2
