class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        start = 0
        n_arithmetic_slices = 0
        for end in range(2, len(A)):
            if A[end] - A[end-1] != A[start+1]-A[start] or end == len(A) - 1:
                # calculate ans
                arr_len = end - start
                if end == len(A) - 1 and A[end] - A[end-1] == A[start+1]-A[start]:
                    arr_len += 1
                if arr_len >= 3:
                    n_arithmetic_slices +=  arr_len*(arr_len-1)//2 - arr_len + 1
                # reset
                start = end - 1
        return n_arithmetic_slices
