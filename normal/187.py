from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = defaultdict(int)
        t = []
        if len(s) <= 10:
            return []
        for i in range(0, len(s)-10+1):
            ans[s[i:i+10]] += 1
        for k, v in ans.items():
            if v >= 2:
                t.append(k)
        return t
