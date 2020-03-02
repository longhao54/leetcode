# 按照官方的思路自己写的
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def ans(left=0, right=len(inorder)-1):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = tmplist[val]
            root.right = ans(index+1, right) 
            root.left = ans(left, index-1)
            return root
        
        tmplist = {val:index for index, val  in  enumerate(inorder)}
        return ans()




# 官方答案
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
 
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
