from collections import defaultdict

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ans = defaultdict(int)
        dp = [root]
        if not root:
            return False
        while dp:
            t = dp.pop()
            ans[t.val] += 1
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        for key in ans:
            t = k - key
            if t == key:
                if ans[key] >= 2:
                    return True
            else:
                if ans.get(t,0) > 0:
                    return True
        return False
