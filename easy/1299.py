class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        ans = [-1]
        for i in arr[-2::-1]:    
            ans.insert(0, m)
            m = max(i, m)
        return ans
