'''

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.check(root, 0, [])[-1]



    def check(self, root, N, List):
        List.append(N)
        if root == None:
            return N
        self.check(root.left, N+1, List)
        self.check(root.right, N+1, List)
        return List



'''
我写的很慢的方法
def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.check(root, 0)
        
    def check(self, root, N):
        if root == None:
            return N
        return max([self.check(root.left, N+1), self.check(root.right, N+1)])
        
        在这里  划重点
        return max(self.check(root.left, N+1), self.check(root.right, N+1))   --- 把列表去掉 速度会快特别多
        
'''

'''

别人写的快一点的方法

return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''