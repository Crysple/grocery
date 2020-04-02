class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                ans[stack.pop()[1]] = n
            stack.append([n, i])
        for n in nums:
            while stack and n > stack[-1][0]:
                ans[stack.pop()[1]] = n
        return ans
        
