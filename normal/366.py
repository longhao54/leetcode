from collections import defaultdict

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        c = float("-inf")
        ans_list = []
        def check(r):
            nonlocal c
            if not r:
                return 0
            a = check(r.left)
            b = check(r.right) 
            dp = max(a, b) + 1
            if dp > len(ans_list):
                ans_list.append([r.val])
            else:
                ans_list[dp-1].append(r.val)
            return dp            
        check(root)
        return ans_list
