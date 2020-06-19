class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        #     <-------------
        #    1   2   3   5  |
        # 1     1/2 1/3 1/5 |
        # 2         2/3 2/5 |
        # 3             3/5 |
        # 5                 V
        def equal(a, b):
            return abs(a-b) <= 10e-9
        total = (len(A)-1) * len(A) //2
        def count(n):
            bigger = 0
            nearest = [0, 1]
            row, col = 0, 1
            while row < len(A) and col <= len(A):
                while col < len(A) and (A[row]/A[col] > n):
                    col += 1
                bigger += col - row - 1
                if col != len(A) and A[row]/A[col] > nearest[0]/nearest[1]: nearest = [A[row], A[col]]
                row += 1
                if col <= row: col += 1
            return total - bigger, nearest
        l, r = 0, 1
        while l < r:
            mid = (l + r) / 2
            rank, _ = count(mid)
            if rank > K:
                r = mid
            elif rank < K:
                l = mid
            else:
                return count(mid)[1]
