from collections import defaultdict

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = defaultdict(int)
        d2 = defaultdict(list)
        tl = []
        dp = [root]
        if not root:
            return []
        while dp:
            t = dp.pop()
            d[t.val] += 1
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        for k, v in d.items():
            d2[v].append(k)
            tl.append(v)
        tl.sort()
        return d2[tl[-1]]
