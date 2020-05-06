import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        endtimes = [intervals[0][1]]
        ans = 1
        for interval in intervals[1:]:
            while endtimes and endtimes[0] <= interval[0]:
                heapq.heappop(endtimes)
            heapq.heappush(endtimes, interval[1])
            ans = max(ans, len(endtimes))
        return ans
                
