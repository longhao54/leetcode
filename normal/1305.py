class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def read(tree):
            if not tree:
                return 
            dp = [tree]
            while dp:
                t = dp.pop()
                ans.append(t.val)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
        read(root1)
        read(root2)
        ans.sort()
        return ans
