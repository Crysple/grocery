class Solution:
    def knightDialer(self, N: int) -> int:
        hop = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]
        ways = [1] * 10
        mod = 10**9 + 7
        for _ in range(N-1):
            nways = [0] * 10
            for n in range(10):
                for next_n in hop[n]:
                    nways[next_n] = (nways[next_n]+ways[n]) % mod
            ways = nways
        return sum(ways) % mod
