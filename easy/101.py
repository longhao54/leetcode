'''

给定一个二叉树，检查它是否是镜像对称的。

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.check(root,root)

    def check(self, q, p):
        if q == None and p == None:
            return True
        if q == None :
            return False
        if p == None:
            return False
        return q.val == p.val and self.check(q.left, p.right) and self.check(q.right, p.left)

'''

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ist(left,right):
            if left == None and right == None: return True;
            if left == None and right != None: return False;
            if left != None and right == None: return False;
            
            return left.val == right.val and ist(left.left,right.right) and ist(left.right,right.left)
        
        if(root == None): return True;
        return ist(root.left,root.right)

'''