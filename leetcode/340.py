class Window:
    def __init__(self):
        self.counter = collections.Counter()
        self.n_unique = 0
    def add(self, c):
        self.counter[c] += 1
        if self.counter[c] == 1:
            self.n_unique += 1
    def remove(self, c):
        self.counter[c] -= 1
        if self.counter[c] == 0:
            self.n_unique -= 1
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = Window()
        lo = hi = ans = 0
        for hi in range(len(s)):
            window.add(s[hi])
            while window.n_unique > k:
                window.remove(s[lo])
                lo += 1
            if window.n_unique <= k:
                ans = max(ans, hi - lo + 1)
        return ans
