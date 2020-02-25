class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        left = 0
        ans = ""
        for i in S:
            if i == "(":
                left += 1
                if left > 1:
                    ans += i
            else:
                left -= 1
                if left >= 1:
                    ans += i
        return ans
