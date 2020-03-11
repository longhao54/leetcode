class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p = p.val
        q = q.val
        ans = None
        def check(r=root):
            nonlocal ans
            if not r:
                return False
            left = check(r.left)
            right = check(r.right)
            mid = r.val in (p,q)
            if left + right + mid >= 2:
                ans = r
            return left or right or mid
        check()
        return ans
