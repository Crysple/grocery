class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        pre_sum = piles[:1]
        for s in piles[1:]:
            pre_sum += (pre_sum[-1] + s),
        pre_sum += 0,
        @lru_cache(None)
        def _stoneGame(start, end):
            if end - start == 1:
                return max(piles[start:end+1])
            return pre_sum[end] - pre_sum[start-1] -\
                    min(_stoneGame(start+1, end), _stoneGame(start, end-1))
        return _stoneGame(0, len(piles)-1)
