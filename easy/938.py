# 较慢 没有利用好二叉搜索树特点
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                if t.val >= L and t.val <= R:
                    ans += t.val
                dp.append(t.left)
                dp.append(t.right)
        return ans

# 快了一点 利用了二叉树的特点
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                if t.val >= L and t.val <= R:
                    ans += t.val
                if t.val > L:
                    dp.append(t.left)
                if t.val < R:
                    dp.append(t.right)
        return ans
