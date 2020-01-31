class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        dp = [root]
        while dp:
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
            for i in range(len(dp) - 1):
                dp[i].next = dp[i+1]
        return root
