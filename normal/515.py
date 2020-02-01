class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dp = [root]
        ans = []
        while dp:
            m = float("-inf")
            for i in range(len(dp)):
                m = max(m, dp[i].val)
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
            ans.append(m)
        return ans  

