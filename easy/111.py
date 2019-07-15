'''

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        deep = self.search(root, 1, [])
        return min(deep)

    def search(self, root, deep, List):

        if not root.left and not root.right:
            List.append(deep)
        else:
            if root.left:
                self.search(root.left, deep + 1, List)
            if root.right:
                self.search(root.right, deep + 1, List)
        return List



class Other_Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 1
        stack = [root]
        while stack:
            level = []
            for i in stack:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
                elif not i.left:
                    return depth
            depth += 1
            stack = level[:]