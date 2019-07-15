'''

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List = self.search(root, [], 0)
        List.reverse()
        return List

    def search(self, root, List, Level):
        if root == None:
            return List
        if len(List) <= Level:
            List.append([])
        List[Level].append(root.val)
        List = self.search(root.left, List, Level+1)
        List = self.search(root.right, List, Level+1)
        return List



'''

class Solution:
    def levelOrderBottom(self, root):
        
        if not root:
            return []
        last=None
        res=[]
        queue=collections.deque([[0,root]])
        while queue:
            depth, node=queue.popleft()
            if node:
                if last==None or last[0]!=depth:
                    res.append([node.val])    
                else:
                    res[-1].append(node.val)
                last=[depth,node]
                queue.append([depth+1,node.left])
                queue.append([depth+1,node.right])
        return res[::-1]

'''