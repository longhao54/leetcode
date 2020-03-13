class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        dp = [(root, 1, root.val, root.val)]
        while dp:
            r, deep, f, gf = dp.pop()
            if not r:
                continue
            dp.append((r.left, deep+1, r.val, f))
            dp.append((r.right, deep+1, r.val, f))
            if deep > 2 and gf%2 ==0:
                ans += r.val
        return ans
