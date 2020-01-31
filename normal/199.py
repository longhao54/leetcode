class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dp = [root]
        ans = []
        while dp:
            ans.append(dp[-1].val)
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
        return ans
