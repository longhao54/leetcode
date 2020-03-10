class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ans = "~"
        def check(r = root, c = ""):
            nonlocal ans
            if not r:
                ans = min(ans, c)
                return ""
            if r.right and r.left or not r.left and not r.right:
                check(r.left, chr(r.val + ord('a'))+c)
                check(r.right, chr(r.val + ord('a')) +c)
            elif not r.right:
                check(r.left, chr(r.val + ord('a'))+c)
            else :
                check(r.right, chr(r.val + ord('a')) +c)
        check()
        return ans
