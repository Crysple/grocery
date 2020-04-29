class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        res = 0
        MOD = 10 ** 9 + 7
        for i in range(N):
            res = (res + ((1<<i) - (1<<(N-i-1))) * A[i]) % MOD
        return res % MOD
