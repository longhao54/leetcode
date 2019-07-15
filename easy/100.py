'''

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p and q or not q and p:
            return False
        a = self.middle_digui(p, [])
        b = self.middle_digui(q, [])
        return a == b

    def middle_digui(self, tree, List):
        List.append(tree.val)
        if tree.left:
            self.middle_digui(tree.left, List)
        else:
            List.append("none")
        if tree.right:
            self.middle_digui(tree.right, List)
        else:
            List.append("none")
        return List


    def other_isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q == None):
            return True
        if (p == None):
            return False
        if (q == None):
            return False
        if (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False