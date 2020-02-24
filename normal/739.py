class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        index, value = [], []
        lenth = len(T)
        ans = [ 0 for i in range(lenth) ]
        for i in range(lenth-1, -1, -1):
            t = T[i]
            while value:
                p = value[-1]
                if t >= p:
                    value.pop()
                    index.pop()
                elif t < p:
                    ans[i] = index[-1] - i
                    value.append(t)
                    index.append(i)
                    break
            value.append(t)
            index.append(i)
        return ans
