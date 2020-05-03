class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lo = hi = 0
        incdp, decdp = collections.deque([0]), collections.deque([0])
        ans = 1
        for hi in range(1, len(nums)):
            #print(decdp, incdp)
            while len(decdp) != 0 and nums[hi] >= nums[decdp[-1]]:
                decdp.pop()
            while len(incdp) != 0 and nums[hi] <= nums[incdp[-1]]:
                incdp.pop()
            decdp.append(hi)
            incdp.append(hi)
            while nums[decdp[0]] - nums[incdp[0]] > limit:
                lo += 1
                while decdp[0] < lo:
                    decdp.popleft()
                while incdp[0] < lo:
                    incdp.popleft()
            ans = max(ans, hi - lo + 1)
        return ans
                
