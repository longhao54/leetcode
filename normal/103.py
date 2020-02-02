class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        left = 1
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
                if left %2 == 1:
                    ans.append(t)
                else:
                    ans.append(t[::-1])
            left += 1
        return ans
