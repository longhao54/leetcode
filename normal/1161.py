class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        check = set()
        c = defaultdict(list)
        dp = [[root, 1]]
        while dp:
            s = 0
            for _ in range(len(dp)):
                t, i = dp.pop(0)
                if t:
                    s += t.val
                    dp.append([t.left, i+1])
                    dp.append([t.right, i+1])
            c[s].append(i)
            check.add(s)
        return min(c[max(check)])
