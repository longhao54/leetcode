class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ans = 0
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                ans += 1
                dp.append(t.left)
                dp.append(t.right)
        return ans
