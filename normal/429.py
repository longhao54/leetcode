class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return 
        ans = []
        dp = [root]
        while dp:
            t_l = []
            for i in range(len(dp)):
                t = dp.pop(0)
                t_l.append(t.val)
                for j in t.children:
                    dp.append(j)
            if t_l:
                ans.append(t_l)
        return ans
