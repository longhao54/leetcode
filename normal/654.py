class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        d_num = {val: i for i, val in enumerate(nums) }
        def check(r, m, start=0, end =len(d_num)):
            mid = d_num[m]
            if start < mid:
                left = max(nums[start:mid])
                l_index = d_num[left]
                r.left = TreeNode(left)
                check(r.left, left, start, l_index)
                check(r.left, left, l_index+1, mid)
            elif not r.left:
                r.left = None
            if mid+1 < end:
                right = max(nums[mid+1: end])
                r_index = d_num[right]
                r.right = TreeNode(right)
                check(r.right, right, mid+1, r_index)
                check(r.right, right, r_index, end)
            elif not r.right:
                r.right = None
            
        m = max(nums)
        root = TreeNode(m)
        check(root, m)
        return root
