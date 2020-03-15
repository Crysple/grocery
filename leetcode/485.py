class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n_ones = max_n = 0
        for i in nums:
            if i == 1:
                n_ones += 1
            elif i == 0:
                max_n = max(max_n, n_ones)
                n_ones = 0
        return max(max_n, n_ones)
