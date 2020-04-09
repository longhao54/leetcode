from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        t = {}
        if not S:
            return []
        for i, v in enumerate(S):
            t[v] = i
        
        ans = [t[S[0]]+1]
        for i, v in enumerate(S[1:]):
            if t[v] > ans[-1]-1:
                if i+1 < ans[-1]-1:
                    ans[-1] = t[v]+1
                else:
                    ans.append(t[v]+1)
        t = [ans[0]]
        for i, v in enumerate(ans[1:]):
            t.append(v - ans[i])
        return t


# 官方答案
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans

