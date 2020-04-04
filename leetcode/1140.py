class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        rest = [0] + piles[-1:]
        for pile in piles[:-1][::-1]:
            rest.append(rest[-1]+pile)
        rest = rest[::-1]

        @lru_cache(None)
        def _get_ans(start, M):
            upper_bound = min(start + 2 * M, len(piles))
            hold = ans = 0
            for i in range(start, upper_bound):
                hold += piles[i]
                opponent_hold = _get_ans(i+1, max(M, i-start+1))
                ans = max(ans, rest[i+1] - opponent_hold + hold)
            return ans
        return _get_ans(0, 1)
