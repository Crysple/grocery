class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - (0 if i == 0 else self.nums[i-1])
