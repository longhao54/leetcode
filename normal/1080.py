# 这个怎么做都错了  看了答案
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def check(root, val = 0):
            nonlocal limit
            val += root.val
            print(root.val, val)
            left = check(root.left, val) if root.left else 0
            right = check(root.right, val) if root.right else 0
            print(root.val, val, left, right)
            if left == "DROP":
                root.left = None
            if right == "DROP":
                root.right = None
            if not root.left and not root.right:
                if val < limit:
                    return "DROP"
        check(root)
        return root

class Solution:

    def __dfs(self, node, s, limit):
        # 先写递归终止条件：如果小于 limit，根据题意，要删除
        if node.left is None and node.right is None:
            return s + node.val < limit

        # 默认为左右结点均剪枝，注意：初值不能设置成 False
        l_tree_deleted = True
        r_tree_deleted = True

        # 如果有左子树，就先递归处理左子树
        if node.left:
            l_tree_deleted = self.__dfs(node.left, s + node.val, limit)

        # 如果有右子树，就先递归处理右子树
        if node.right:
            r_tree_deleted = self.__dfs(node.right, s + node.val, limit)

        # 左右子树是否删除的结论得到了，由自己来执行是否删除它们
        if l_tree_deleted:
            node.left = None
        if r_tree_deleted:
            node.right = None

        # 只有左右子树都被删除了，自己才没有必要保留
        return l_tree_deleted and r_tree_deleted

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        root_deleted = self.__dfs(root, 0, limit)
        if root_deleted:
            return None
        return root
