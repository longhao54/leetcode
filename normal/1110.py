# 很慢的方法 
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return 
        ans = []
        
        def delete(tree, to_delete):
            dp = [tree]
            if not tree:
                return 
            if tree.val in to_delete:
                delete(tree.left, to_delete)
                delete(tree.right, to_delete)
                tree = None
            while dp:
                t = dp.pop()
                if t.left:
                    dp.append(t.left)
                    if t.left.val in to_delete:
                        delete(t.left, to_delete)
                        t.left = None
                if t.right:
                    dp.append(t.right)
                    if t.right.val in to_delete:
                        delete(t.right, to_delete)
                        t.right = None
                
            if tree and tree not in ans:
                ans.append(tree)

        delete(root, to_delete)
        return ans

# 较快答案
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return []
        if not to_delete: return [root]
        to_delete_set = set(to_delete)
        res = []
        if root.val not in to_delete_set:
            res.append(root)

        def dfs(root):
            if not root: return
            left, right = root.left, root.right
            if root.val in to_delete_set:
                if left and left.val not in to_delete_set:
                    res.append(left)
                if right and right.val not in to_delete_set:
                    res.append(right)
            if left and left.val in to_delete_set: root.left = None
            if right and right.val in to_delete_set: root.right = None
            dfs(left)
            dfs(right)
        dfs(root)
        return res
