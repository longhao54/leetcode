class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0
        def check(r=root):
            nonlocal ans
            if not r:
                return 0
            left = check(r.left)
            right = check(r.right)
            t = abs(left-right)
            ans += t
            return left+right+r.val
        check()
        return ans
