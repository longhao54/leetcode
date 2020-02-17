class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        ans = []
        dp = [root]
        d = {}
        if not root:
            return root
        while dp:
            t = dp.pop()
            ans.append(t.val)
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        ans.sort()
        for i, v in enumerate(ans):
            d[v] = i
        lenth = len(ans)
        for i in range(lenth-2, -1, -1):
            ans[i] += ans[i+1]
        dp = [root]
        while dp:
            t = dp.pop()
            t.val = ans[d[t.val]]
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        return root
