class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        ans = 0
        def check(r = root):
            nonlocal ans
            if not r:
                return []
            left = check(r.left)
            right = check(r.right)
            t = set(left+right)
            if len(t) == 0:
                ans += 1
                return [r.val]
            elif r.val in t and len(t) == 1:
                ans += 1
                return [r.val]
            else:
                return left+right+[r.val]
        check()
        return ans
