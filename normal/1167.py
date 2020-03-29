# 这个超时了
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks.sort()
        l = len(sticks)
        ans = 0
        while l > 1:
            t1 = sticks.pop(0)
            t2 = sticks.pop(0)
            p = t1+t2
            ans += p
            c = 0
            c1 = True
            for i in sticks:
                if i >= p:
                    sticks.insert(c, p)
                    c1 = False
                    break
                c += 1
            if c1:
                sticks.append(p)
            l -= 1
        return ans

# 用库的答案
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        from heapq import * 
        heapify(sticks) # 建优先级队列
        res = 0
        while len(sticks) > 1:
            s1 = heappop(sticks) #找到最短的棒材
            s2 = heappop(sticks) #找到第二短的棒材
            res += s1 + s2 #把最短的两根棒子连接在一起
            heappush(sticks, s1 + s2) #把连接好的棒材放进队
        return res 
