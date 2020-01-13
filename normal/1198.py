# 对于每个行 用二分查找 判断上一行的元素是否在 这个应该是会更快一些 比直接in



class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ans = mat[0]
        for j in mat[1:]:
            ans = [ i for i in ans if i in j]
            if not ans:
                return -1
        return min(ans)
