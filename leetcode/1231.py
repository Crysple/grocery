class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 0, sum(sweetness) // (K+1) + 1
        while l < r:
            mid = l + (r - l) // 2
            k, csum = 0, 0
            for s in sweetness:
                csum += s
                if csum >= mid:
                    k += 1
                    csum = 0
            #print(l, r, mid, k)
            if k >= K + 1:
                l = mid + 1
            else:
                r = mid
        return l - 1
