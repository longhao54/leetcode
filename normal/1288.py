class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda u: (u[0], -u[1]))
        ans, rmax = n, intervals[0][1]
        for i in range(1, n):
            if intervals[i][1] <= rmax:
                ans -= 1
            else:
                rmax = max(rmax, intervals[i][1])
        return ans
