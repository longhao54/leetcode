class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        s = 0
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                s += t.val
                dp.append(t.left)
                dp.append(t.right)
        ans = 0
        def check(r = root):
            nonlocal ans, s
            if not r:
                return 0
            left = check(r.left)
            right = check(r.right)
            p = left + right + r.val
            ans = max(ans, p * (s-p))
            return p
        check()
        return ans % 1000000007
