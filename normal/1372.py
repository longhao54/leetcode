class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        dp = [(root.left, "l", 1), (root.right, "r", 1)]
        ans = 0
        while dp:
            r, w, c = dp.pop()
            if r:
                ans = max(ans, c)
                if w == "l":
                    dp.append((r.right, "r", c+1))
                    dp.append((r.left, "l", 1))
                else:
                    dp.append((r.right, "r", 1))
                    dp.append((r.left, "l", c+1))
        return ans
