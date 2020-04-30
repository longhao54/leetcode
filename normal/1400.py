from collections import defaultdict
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dic = defaultdict(int)
        c = 0
        one = 0
        for i in s:
            c += 1
            dic[i] += 1
            if dic[i] % 2 == 1:
                one += 1
            else:
                one -= 1
        if c == k:
            return True
        if c < k or one > k:
            return False
        return True
