# 差点超时 暴力解法
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in g:
            for index, value in enumerate(s):
                if value >= i:
                    s.pop(index)
                    count += 1
                    break
        return count

# 优化的暴力破解
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        start = 0
        lenth = len(s)
        for i in g:
            if start >= lenth:
                break
            for j in range(start, lenth):
                if s[j] >= i:
                    s.pop(start)
                    count += 1
                    lenth -= 1
                    break
                else:
                    start += 1
        return count


# 最快答案 双指针思路
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child,cookie = 0,0
        len_g = len(g)
        len_s = len(s)
        while (child < len_g) and (cookie < len_s) :
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
