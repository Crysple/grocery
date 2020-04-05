class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        s = '!#' + '#'.join(s) + '#@'
        p, frontier, center = [1] * len(s), 2, 1
        longest_substr = 0
        for i in range(2, len(s)-2):
            if i < frontier:
                p[i] = min(p[2*center-i], frontier-i)
            while s[i+p[i]] == s[i-p[i]]:
                p[i] += 1
            if i+p[i] > frontier:
                frontier = i+p[i]
                center = i
            if p[i] > p[longest_substr]:
                longest_substr = i
        return s[longest_substr-p[longest_substr]+1:longest_substr+p[longest_substr]].replace('#', '')
