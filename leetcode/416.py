class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        target = s // 2
        @lru_cache(None)
        def subsetSum(pos, cursum):
            if cursum == target:
                return True
            if pos == len(nums) or cursum > target:
                return False
            return subsetSum(pos+1, cursum+nums[pos])\
                    or subsetSum(pos+1, cursum)
        return subsetSum(0, 0)

