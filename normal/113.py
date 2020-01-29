class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        dp = [(root, [], sum)]
        while dp:
            r, t, s = dp.pop()
            if not r.left and not r.right and s == r.val:
                ans.append(t+[r.val])
            if r.left:
                dp.append((r.left, t+[r.val], s-r.val))
            if r.right:
                dp.append((r.right, t+[r.val], s-r.val))
        return ans
