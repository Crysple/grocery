class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # O(n) dp
        if len(nums) < 2:
            return len(nums)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)
        # Greedy
        def check(i):
            return nums[i]<nums[i+1]>nums[i+2] or nums[i]>nums[i+1]<nums[i+2]
        nums = nums[:1] + [nums[i] for i in range(1, len(nums)) if nums[i]!=nums[i-1]]
        return sum(check(i) for i in range(len(nums)-2)) + min(2, len(set(nums)))
            
        # First thought O(n^2) dp
        if not nums:
            return 0
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1]+1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1)
        return max([max(i) for i in dp])
