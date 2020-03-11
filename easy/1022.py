class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        nums = []
        def check(r = root , s = 0):
            if not r.left and not r.right:
                nums.append(s*10+r.val)
                return None
            if r.left:
                check(r.left, s*10+r.val)
            if r.right:
                check(r.right, s*10+r.val)
            
        check()
        s = 0
        for i in nums:
            s += int(str(i), 2)
        return s
