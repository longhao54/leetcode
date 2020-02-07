class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = []
        right = []
        lenth = len(s)
        s = list(s)
        for index, value in enumerate(s):
            if value == "(":
                right.append(index)
            if value == ")":
                if right:
                    right.pop()
                else:
                    left.append(index)
        left += right
        left.sort()
        for i in left[::-1]:
            s.pop(i)
        return "".join(s)
