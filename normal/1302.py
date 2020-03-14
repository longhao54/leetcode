class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        dp = [root]
        ans = 0
        if not root:
            return ans
        while dp:
            ans = 0
            for i in range(len(dp)):
                t = dp.pop(0)
                ans += t.val
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
        return ans

