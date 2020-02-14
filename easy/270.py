class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = None
        c = float("inf")
        dp = [root]
        while dp:
            t = dp.pop()
            if abs(t.val-target) < c:
                c = abs(t.val-target)
                ans = t.val
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        return ans
