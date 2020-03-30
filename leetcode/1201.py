from functools import reduce
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        factors = [a, b, c]

        def cal_gcd(x, y):
            if x != 0:
                return cal_gcd(y%x, x)
            return y

        def cal_lcm(x, y):
            return x // cal_gcd(x, y) * y

        def get_num_rank(num):
            nth = sum([num//f for f in factors])
            nth -= sum([num//lcm for lcm in lcms])
            nth += num//alllcm
            return nth

        lcms = [cal_lcm(a, b), cal_lcm(a, c), cal_lcm(b, c)]
        alllcm = cal_lcm(lcms[0], c)
        

        l = 0
        r = 2 * (10 ** 9) + 1
        while l < r:
            m = l + (r - l) // 2
            nth = get_num_rank(m)
            if nth < n:
                l = m + 1
            elif nth > n or not any([m%f==0 for f in factors]):
                r = m
            else:
                return m

