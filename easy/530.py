class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = []
        dp = [root]
        while dp:
            t = dp.pop()
            ans.append(t.val)
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        ans.sort()
        lenth = len(ans)
        m = float("inf")
        for i in range(1, lenth):
            m = min(abs(ans[i] - ans[i-1]), m)
        return m
