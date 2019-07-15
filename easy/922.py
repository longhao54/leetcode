class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = []
        ans_b = []
        for i in A:
            if i % 2 == 0:
                ans.append(i)
            else:
                ans_b.append(i)
        c = []
        for a,b in zip(ans,ans_b):
            c += [a,b]
        return c
