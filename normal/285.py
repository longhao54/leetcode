class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ans = float('inf')
        dp = [root]
        v = p.val
        anser = ""
        while dp:
            t = dp.pop()
            if t:
                if t.val > v and t.val < ans:
                    anser = t    
                    ans = t.val
                dp.append(t.left)
                dp.append(t.right)
        return anser
