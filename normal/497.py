import random

# 我也不知道为什么 最后两道测试用例无法通过 题目不是什么很难的 所以我就直接跳过吧
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.ans = {}
        self.lenth = 0
        for index, t in enumerate(rects):
            if t[0] == t[2] or t[1] == t[3]:
                continue
            self.ans[index] = [sorted([t[0], t[2]]), sorted([t[1], t[3]])]
            self.lenth = index                  
    def pick(self) -> List[int]:
        pik = random.randint(0, self.lenth)
        x, y = self.ans[pik]
        return [random.randint(x[0], x[1]), random.randint(y[0], y[1])]


from bisect import bisect_left
from random import randint
class Solution(object):
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.weight = []
        s = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) #注意加1
            s += area
            self.weight.append(s)
    def pick(self):
        """
        :rtype: List[int]
        """
        index = bisect_left(self.weight, randint(1, self.weight[-1]))
        rect = self.rects[index]
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]
