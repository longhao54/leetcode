class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        dp = [root]
        while dp:
            t = []
            for i in range(len(dp)):
                r = dp.pop(0)
                t.append(r.val)
                if r.left:
                    dp.append(r.left)
                if r.right:
                    dp.append(r.right)
            if t:
                ans.append(t)
        return ans
