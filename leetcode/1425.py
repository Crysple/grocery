class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = collections.deque([[0,nums[0]]])
        for i in range(1, len(nums)):
            if dq[0][1] > 0:
                nums[i] += dq[0][1]
            while dq and dq[-1][1] <= nums[i]:
                dq.pop()
            dq.append([i, nums[i]])
            while dq and dq[0][0] + k <= i:
                dq.popleft()
        return max(nums)
