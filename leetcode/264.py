import bisect
class Ugly:
    def __init__(self):
        n = 1690
        factors = [2, 3, 5]
        ugly_nums = [1]
        pointers = [0, 0, 0]
        pos = 1
        while pos < n:
            next_ugly_nums = [ugly_nums[pointers[i]] * factors[i] for i in range(3)]
            min_ugly_num = min(next_ugly_nums)
            ugly_nums.append(min_ugly_num)
            for i in range(3):
                if min_ugly_num == next_ugly_nums[i]:
                    pointers[i] += 1
            pos += 1
        self.ugly_nums = ugly_nums
class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.ugly_nums[n-1]
        
