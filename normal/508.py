from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        d1 = defaultdict(int)
        d2 = defaultdict(list)
        m = float("-inf")
        def check(r=root):
            if not r:
                return 0
            left = check(r.left)
            right = check(r.right)
            t = left +right + r.val
            d1[t] += 1
            return t
        check()
        for k, v in d1.items():
            d2[v].append(k)
            m = max(m, v)
        return d2[m]
