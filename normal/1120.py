class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        a = float("-inf")
        def check(r=root):
            nonlocal a
            if not r:
                return 0,0
            left, lc = check(r.left)
            right, rc = check(r.right)
            s = left + right + r.val
            c = lc+rc+1
            a = max(a, s / c)
            return s, c
        check()
        return a
