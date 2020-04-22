class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        import collections
        n = len(wall)
        res = []
        for zhuanqiang in wall:
            if len(zhuanqiang) == 1:
                continue
            sum = 0
            for i in range(0,len(zhuanqiang)-1):
                sum = zhuanqiang[i] = sum + zhuanqiang[i]
                res.append(sum)
        d = dict(collections.Counter(res))
        ans = len(wall)
        for i in d:
            ans = min(ans,n - d[i])
        return ans
