class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '!#'+'#'.join(s) + '#@'
        p = len(s) * [1] # point to
        farthest = 1
        center = 0
        for i in range(1, len(s)-1):
            if i < farthest:
                mirror_i = 2 * center - i
                p[i] = min(p[mirror_i], farthest-i)
            while s[i+p[i]] == s[i-p[i]]:
                p[i] += 1
            if i + p[i] > farthest:
                farthest = i + p[i]
                center = i
        return sum(v//2 for v in p)
