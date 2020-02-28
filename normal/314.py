from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        row = 0
        if not root:
            return []
        s, m = float("inf"), float("-inf")
        dp = [(root, row)]
        ans = defaultdict(list)
        while dp:
            t, n = dp.pop(0)
            if t:
                s = min(s, n)
                m = max(m, n)
                ans[n].append(t.val)
                dp.append((t.left, n-1))
                dp.append((t.right, n+1))
        t = []
        for i in range(s, m+1):
            if ans[i]:
                t.append(ans[i])
        return t
