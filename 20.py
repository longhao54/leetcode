'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''

#
# class Solution:
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         in_keys = {"(":")", "{":"}", "[":"]"}
#         out_keys = {")":"(","}":"{","]":"["}
#         IN, OUT = [" "], [" "]
#         check = False
#         if not s.split():
#             return True
#         for i in s:
#             if i in in_keys:
#                 IN.append(i)
#                 OUT.append(in_keys[i])
#             elif i in out_keys:
#                 last_in = out_keys[i]
#                 if last_in == IN[-1] and i == OUT[-1]:
#                     IN.pop()
#                     OUT.pop()
#                     check=True
#                 else:
#                     check = False
#                     break
#         if len(IN) !=1 or len(OUT)!=1 :
#             return False
#         return check


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'(','[','{'}
        map = {')':'(',']':'[','}':'{'}
        stack = []
        for val in s:
            if val in left:
                stack.append(val)
            elif stack and map[val] == stack.pop():
                continue
            else:
                return False
        if stack: return False
        return True

A=Solution()
print(A.isValid("([)]"))