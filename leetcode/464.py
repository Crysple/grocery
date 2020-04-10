class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if sum(range(maxChoosableInteger+1)) < desiredTotal:
            return False
        N = 1 << maxChoosableInteger
        @lru_cache(None)
        def canIWin(state, total):
            # print(bin(state), total)
            if state == 0:
                return False
            if len(bin(state)) - 2 >= total:
                return True
            for i in range(maxChoosableInteger):
                if (1 << i) & state:
                    if not canIWin(state ^ (1 << i), total-i-1):
                        return True
            return False
        return canIWin(N-1, desiredTotal)
