class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ans = mat[0]
        for j in mat[1:]:
            ans = [ i for i in ans if i in j]
            if not ans:
                return -1
        return min(ans)
