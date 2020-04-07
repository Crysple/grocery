import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        dp = [1] * len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        sorted_arr = []
        for i in range(len(envelopes)):
            pos = bisect.bisect_left(sorted_arr, (envelopes[i][1], 0))

            subenv = sorted_arr[pos-1][1]+1 if pos > 0 else 1
            if pos < len(sorted_arr):
                subenv = max(subenv, sorted_arr[pos][1])
                sorted_arr[pos] = (envelopes[i][1], subenv)
            else:
                sorted_arr += (envelopes[i][1], subenv),

        return max([item[1] for item in sorted_arr])
