class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))
