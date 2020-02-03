class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        dp = []
        if root.left: 
            dp.append((root.left, 1))
        if root.right:
            dp.append((root.right, 0))
        while dp:
            for i in range(len(dp)):
                t, c = dp.pop(0)
                if not t.left and c and not t.right:
                    ans += t.val
                if t.left:
                    dp.append((t.left, 1))
                if t.right:
                    dp.append((t.right, 0))
        return ans
