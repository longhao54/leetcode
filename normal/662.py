class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 1
        dp = [(root,1)]
        while dp:
            s, m = float('inf'), float('-inf')
            l = len(dp)
            for i in range(l):
                t, i = dp.pop(0)
                if t.left:
                    dp.append((t.left, i*2))
                if t.right:
                    dp.append((t.right, i*2+1))
                s = min(s, i)
                m = max(m, i)
            ans = max(m-s+1, ans)
        return ans
