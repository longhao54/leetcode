# 做法感觉没问题 但是题目好像没有理解清楚 不知道要求的边数指的是什么东西
# 所以抄了答案
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = [0]
        if not root:
            return 0
        def backtrace(node, now="", count=1):
            if not node:
                ans.append(count)
                return ""
            if node.val == now:
                count += 1
            else:
                ans.append(count)
                count = 1
            backtrace(node.left, node.val, count)
            backtrace(node.right, node.val, count)

        if root.left:
            backtrace(root.left)
        if root.right:
            backtrace(root.right)
        return max(ans)


# 抄的答案
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
