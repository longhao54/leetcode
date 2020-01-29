class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = 1
        Max = 1
        dp = [(root, ans)]
        while dp:
            t, ans = dp.pop()
            if t.children:
                ans += 1
                for i in t.children:
                    dp.append((i, ans))
            Max = max(ans, Max)
        return Max
