import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Binary search version
#         n, m = len(mat), len(mat[0])

#         def countSubarraySmallerOrEqual(target_sum, row, need):
#             if target_sum < 0: return 0
#             if row == n: return 1
#             n_subarray = 0
#             for col in range(m):
#                 cnt = countSubarraySmallerOrEqual(target_sum-mat[row][col], row+1, need-n_subarray)
#                 n_subarray += cnt
#                 if n_subarray > need or cnt == 0:
#                     break
#             return n_subarray

#         l, r = 0, sum(row[-1] for row in mat) + 1
#         while l < r:
#             mid = (l + r) // 2
#             if countSubarraySmallerOrEqual(mid, 0, k) >= k:
#                 r = mid
#             else:
#                 l = mid + 1
#         return l

        # original ans: bfs + heap
        root = [0] * len(mat)
        root_sum = sum(mat[i][root[i]] for i in range(len(mat)))
        cache = {root_sum: [root]}
        visited = dict()
        queue = [root_sum]
        for _ in range(k-1):
            #print(queue, cache)
            cursum = queue[0]
            config = list(cache[cursum].pop())
            visited[tuple(config)] = True
            if len(cache[cursum]) == 0:
                heapq.heappop(queue)
                del cache[cursum]

            for i in range(len(mat)):
                if config[i] < len(mat[i]) - 1:
                    config[i] += 1
                    nconfig = tuple(config)
                    config[i] -= 1
                    nsum = cursum -  mat[i][nconfig[i]-1] + mat[i][nconfig[i]]
                    if nconfig not in visited:
                        visited[nconfig] = True
                        if nsum in cache:
                            cache[nsum].append(nconfig)
                        else:
                            cache[nsum] = [nconfig]
                            heapq.heappush(queue, nsum)
        return queue[0]
