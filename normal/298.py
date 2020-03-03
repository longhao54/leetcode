class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        ans = float("-inf")
        dp = [(root, 1, ans)]
        while dp:
            t, c, val = dp.pop()
            if t:
                if t.val == val+1:
                    c += 1
                else:
                    c = 1
                ans = max(c, ans)
                dp.append((t.left, c, t.val))
                dp.append((t.right, c, t.val))
        return ans if ans != float("-inf") else 0
