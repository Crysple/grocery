class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:(x[0],-x[1]))
        ans = intervals[:1]
        for itv in intervals[1:]:
            if itv[0] >= ans[-1][1]:
                ans.append(itv)
            elif itv[1] > ans[-1][1]:
                ans.append(itv)
        return len(ans)
