class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        dp = [root]
        count = 0
        while dp:
            count += 1
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                if t.right:
                    dp.append(t.right)
        ans = [[""]*(2**count -1) for i in range(count)]
        dp = [(root, 0, 2**count -1, 0)]
        while dp:
            t = dp.pop()
            if t[0]:
                node, start, end, m = t
                mid = (start + end) // 2
                ans[m][mid] = str(node.val)
                dp.append((node.left, start, mid, m+1))
                dp.append((node.right, mid, end, m+1))
        return ans
