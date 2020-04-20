class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = [""]
        for i in s:
            if i == "(":
                ans.append('')
            elif i == ")":
                ans[-2] += ans[-1][::-1]
                ans.pop()
            else:
                ans[-1] += i
        return ans[0]
