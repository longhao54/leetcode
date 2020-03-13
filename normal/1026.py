class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = float('-inf')
        dp = [(root, root.val, root.val)]
        while dp:
            t, m, s = dp.pop()
            if t:
                ans = max(ans, abs(m-t.val), abs(s-t.val))
                dp.append((t.left, max(t.val,m), min(t.val, s)))
                dp.append((t.right, max(t.val,m), min(t.val, s)))
        return ans
