class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        if len(stones) < 3:
            return [0, 0]

        stones = sorted(stones)
        n = len(stones)
        
        high = max(stones[-2]-stones[0]-n, stones[-1]-stones[1]-n) + 2
        start = end = 0
        low = n + 1
        for end in range(n):
            while stones[end]-stones[start] >= n:
                start += 1
            if end-start+1 == n-1 and stones[end]-stones[start] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n-(end-start+1))
        return low, high
