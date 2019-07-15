class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        ri = []
        for i in A:
            if i % 2 == 0:
                ans.append(i)
            else :
                ri.append(i)
        return ans + ri
