class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals) <= 1:
            return True
        start = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < start:
                return False
            start = i[1]
        return True

    def fast(self, intervals):
        intervals.sort(key=lambda x:x.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
