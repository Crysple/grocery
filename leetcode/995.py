class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n_flips = 0
        flips = [0] * len(A)
        flip = 0
        for i in range(len(A)):
            flip ^= flips[i]
            A[i] ^= flip
            if A[i] == 0:
                if i >= len(A) - K + 1:
                    return -1
                n_flips += 1
                flip ^= 1
                if i+K < len(A):
                    flips[i+K] ^= 1
            
        return n_flips
