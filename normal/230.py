class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                ans.append(t.val)
                dp.append(t.left)
                dp.append(t.right)
        ans.sort()
        return ans[k-1]
