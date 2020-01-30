class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        dp = [root]
        while dp:
            for i in range(len(dp)):
                t = dp.pop(0)
                if not t.left:
                    continue
                dp.append(t.left)
                dp.append(t.right)
            for j in range(len(dp)-1):
                dp[j].next = dp[j+1]
        return root
