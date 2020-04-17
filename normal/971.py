
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []
        n = 0
        def check(r):
            nonlocal n, ans
            if r:
                if r.val != voyage[n]:
                    ans=[-1]
                    return ""
                n += 1
                if n < len(voyage) and r.left and r.left.val != voyage[n]:
                    ans.append(r.val)
                    check(r.right)
                    check(r.left)
                    
                else:
                    check(r.left)
                    check(r.right)
        
        check(root)
        if -1 in ans:
            return ans
        return ans
