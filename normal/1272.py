class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = list()
        toL, toR = toBeRemoved
        for x, y in intervals:
            if toL >= y or toR <= x:
                ans.append([x, y])
            else:
                if toL > x:
                    ans.append([x, toL])
                if toR < y:
                    ans.append([toR, y])
        return ans
