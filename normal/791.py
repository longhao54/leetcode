from collections import defaultdict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        tmp = defaultdict(int)
        for i in T:
            tmp[i] += 1
        ans = ""
        for i in S:
            if i in tmp:
                ans += i*tmp[i]
                tmp.pop(i)
        for k, v in tmp.items():
            ans += v*k
        return ans
