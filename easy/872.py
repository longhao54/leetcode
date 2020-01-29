class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        r1 = self.check(root1)
        r2 = self.check(root2)
        return r1 == r2

    def check(self, root):
        ans = []
        dp = [root]
        while dp:
            t = dp.pop()
            if not t.left and not t.right:
                ans.append(t.val)
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        return ans
