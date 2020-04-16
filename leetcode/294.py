class Solution:
    def canWin(self, s: str) -> bool:
        @lru_cache(None)
        def canWin(s):
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    if not canWin(s[:i] + '--' + s[i+2:]):
                        return True
            return False
        return canWin(s)
