# 执行比较慢  擦边过
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, check = []):
            nonlocal ans
            if not root.left and not root.right:
                check[root.val-1] += 1
                c = 0
                for i in check:
                    if i % 2 != 0:
                        c += 1
                if c <= 1:
                    ans += 1
            
            if root.left:
                dfs(root.left, check[0:root.val-1]+[check[root.val-1]+1] + check[root.val:])
            if root.right:
                dfs(root.right, check[0:root.val-1]+[check[root.val-1]+1] + check[root.val:])
        
        dfs(root, [0]*9)
        return ans


# 快的方法

