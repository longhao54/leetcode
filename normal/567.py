from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sd1 = defaultdict(int)
        sd2 = defaultdict(int)
        l = len(s1)
        for i in s1:
            sd1[i] += 1
        left = 0
        for j in s2[left:l]:
            sd2[j] += 1
        if sd1 == sd2:
            return True
        while left + l  < len(s2):
            t = s2[left]
            sd2[t] -= 1
            if sd2[t] == 0:
                sd2.pop(t)
            left += 1
            sd2[s2[left+l-1]] += 1
            if sd2 == sd1:
                return True
        return False
