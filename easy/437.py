class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        dp = [[root, []]]
        if not root:
            return 0
        count = 0
        while dp:
            for i in range(len(dp)):
                r, t = dp.pop()
                c = [r.val]
                for j in t:
                    c.append(j+r.val)
                if r.left:
                    dp.append([r.left, c])
                if r.right:
                    dp.append([r.right, c])
                for k in c:
                    if k == sum:
                        count += 1
        return count
