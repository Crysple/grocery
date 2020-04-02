class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        uniques = 91 # from 2
        numerator = [0, 9]
        for i in range(8):
            numerator += numerator[-1] * (9 - i - 1),
        for i in range(3, min(n+1, 11)):
            uniques += 9 * numerator[i-1]
        return uniques

