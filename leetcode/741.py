class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        @lru_cache(None)
        def cherryPickup(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1==N or c1 == M or r2 == N or c2 == M or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            if r1==N-1 and c1==M-1 or r2==N-1 and c2==M-1:
                return grid[N-1][M-1]
            if r1==r2:
                gain = grid[r1][c1]
            else:
                gain = grid[r1][c1] + grid[r2][c2]
            return gain + max([cherryPickup(r1+1, c1, r2+1),
                        cherryPickup(r1+1, c1, r2),
                        cherryPickup(r1, c1+1, r2+1),
                        cherryPickup(r1, c1+1, r2)])
        res = cherryPickup(0, 0, 0)
        return res if res != -float('inf') else 0
