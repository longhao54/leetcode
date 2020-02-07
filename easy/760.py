from collections import defaultdict
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        B = self.check(B)
        ans = []
        for i in A:
            ans.append(B[i].pop())
        return ans

    def check(self, T):
        t = defaultdict(list)
        for i, v in enumerate(T):
            t[v].append(i)
        return t
