# 这两种方法 运行时间都是在 95ms左右
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        right, left = 0, 0
        for i in S:
            if i == "(":
                right += 1
            elif i == ")":
                if right > 0:
                    right -= 1
                else:
                    left += 1
        return left + right

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while "()" in S:
            S = S.replace("()","")
        return len(S)


