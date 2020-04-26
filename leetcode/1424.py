class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        rest_row = []
        max_len = max(len(l) for l in nums)
        for left_most_i in range(max_len+len(nums)-1):
            nrest_row = []
            for row in [left_most_i] + rest_row:
                j = left_most_i - row
                if row < len(nums) and j < len(nums[row]):
                    ans.append(nums[row][j])
                    nrest_row.append(row)
            rest_row = nrest_row
        return ans
