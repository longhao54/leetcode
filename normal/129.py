class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        dp = [(root, root.val)]
        while dp:
            t, s = dp.pop()
            if not t.left and not t.right:
                ans += s
            if t.left:
                dp.append((t.left, s*10+t.left.val))
            if t.right:
                dp.append((t.right, s*10 + t.right.val))
        return ans
