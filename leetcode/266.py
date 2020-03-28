from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        has_center = False
        for v in counter.values():
            if v & 1:
                if has_center:
                    return False
                has_center = True
        return True
