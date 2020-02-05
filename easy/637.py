class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        dp = [root]
        while dp:
            c = 0
            l = len(dp)
            for i in range(l):
                i = dp.pop(0)
                c += i.val
                if i.left:
                    dp.append(i.left)
                if i.right:
                    dp.append(i.right)
            ans.append(c/l)
        return ans
