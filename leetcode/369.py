class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        groups = dict()
        for n in nums:
            longest = []
            for repre in groups:
                if n % repre == 0:
                    if len(longest) < len(groups[repre]):
                        longest = groups[repre]
            groups[n] = longest + [n]
        return max(groups.values(), key=lambda x:len(x)) if groups else []
