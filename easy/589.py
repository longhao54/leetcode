class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        dp = [root]
        if not root:
            return []
        while dp:
            t = dp.pop()
            ans.append(t.val)
            for i in t.children[::-1]:
                dp.append(i)
        return ans
