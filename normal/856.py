class Solution(object):
    def scoreOfParentheses(self, S):
        ans = [0] 
        for x in S:
            if x == '(':
                ans.append(0)
            else:
                v = ans.pop()
                ans[-1] += max(2 * v, 1)

        return ans.pop()
