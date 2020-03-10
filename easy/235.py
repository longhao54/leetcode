class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dp = [root]
        p = p.val
        q = q.val
        if p > q:
            q, p = p, q
        c = set([q, p])
        while dp:
            t = dp.pop()
            value = t.val
            if p < value and q > value or value in c:
                return t
            elif p < value and q < value:
                dp.append(t.left)
            else:
                dp.append(t.right)
        return None
