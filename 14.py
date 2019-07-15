'''
输入: ["flower","flow","flight"]
输出: "fl"
'''


# class Solution:  # 我做的
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         index = 0
#         if len(strs) == 1:
#             return strs[0]
#         try:
#             w = strs[0]
#             lenth = len(strs[1:])
#             while index +1 <= len(w):
#                 for i, lines in enumerate(strs[1:]):
#                     if w[index] != lines[index]:
#                         return index
#                     if lenth - i == 1:
#                         index += 1
#         except Exception as e:
#             pass
#         finally:
#             return "" if not index else strs[0][0:index]


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for x, y in enumerate(shortest):
            for s in strs:
                if s[x]!=y:
                    return shortest[:x]
        return shortest

a = Solution()
print(a.longestCommonPrefix(["aa","ab"]))