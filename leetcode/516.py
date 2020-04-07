class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def longestPalindromeSubseq(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + longestPalindromeSubseq(i+1, j-1)
            return max(longestPalindromeSubseq(i+1, j),
                        longestPalindromeSubseq(i, j-1))
        return longestPalindromeSubseq(0, len(s)-1)
