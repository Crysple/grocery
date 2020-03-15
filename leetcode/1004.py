class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = end = max_len = n_zeros = 0
        for end in range(len(A)):
            if A[end] == 0:
                n_zeros += 1
            if n_zeros == K + 1:
                max_len = max(max_len, end - start)
                start += A[start:].index(0) + 1
                n_zeros -= 1
        return max(max_len, end - start + 1)
