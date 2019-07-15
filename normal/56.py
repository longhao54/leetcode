class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = []
        start = intervals[0]
        ans.append(start)
        for i in intervals[1:]:
            if i[0] <= ans[-1][1] :
                if i[1] >= ans[-1][1]:
                    ans[-1] = [ans[-1][0], i[1]]
            else:
                ans.append(i)
        return ans
