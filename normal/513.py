class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 
        dp = [root]
        ans = ""
        while dp:
            ans = dp[0].val
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
        return ans
