class Solution:
    def countArrangement(self, N: int) -> int:
        @lru_cache(None)
        def permutate(idx, rest):
            if idx == N+1:
                return 1
            ans = 0
            for n in range(N):
                if (1<<n) & rest and ((n+1) % idx == 0 or idx % (n+1) == 0):
                    ans += permutate(idx+1, rest^(1<<n))
            return ans
        return permutate(1, (1<<N)-1)
