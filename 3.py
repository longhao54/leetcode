'''
给定一个字符串，找出不含有重复字符的最长子串的长度。

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

'''

# def check(string):
#     if len(string) != len(set(string)):
#         return False
#     return True

# def get_son_string(stiring, son_len, lenth):
#     count = lenth - son_len + 1
#     start_index = 0
#     end_index = start_index + son_len
#     for i in range(count):
#         line = stiring[start_index:end_index]
#         if check(line):
#             return True
#         else:
#
#             start_index += 1
#             end_index += 1
#
#
#         if end_index > lenth:
#             return False
#
#
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         lenth = len(s)
#         son_len = lenth
#
#
#         while True:
#
#             if get_son_string(s, son_len, lenth):
#                 return son_len
#             else:
#                 son_len -= 1
#                 if son_len == 0:
#                     return None

# def get_son_string(line, start, count, lenth):
#     while True:
#
#         if check(line[start:start+count]):
#             count += 1
#             if start + count > lenth:
#                 return count
#         else:
#             return count

# def check(string):
#     if len(string) != len(set(string)):
#         return False
#     return True
#
# def get_son_string(line, start, count, lenth):
#     temp = set()
#     while True:
#         temp = set(line[start:start+count])
#         if len(temp) == count:
#             count += 1
#         else:
#             return count
#
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if not s:
#             return 0
#         lenth = len(s)
#         if lenth == 1:
#             return 1
#         max_num = 1
#         start = 0
#         while True:
#             max_num = get_son_string(s, start, max_num, lenth)
#
#             if start + max_num >= lenth:
#                 return max_num -1
#             start += 1

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        longest = 0
        last = dict()

        for i, char in enumerate(s):
            if (char in last) and (last[char] >= left):
                if i - left > longest:
                    longest = i - left
                left = last[char] + 1
            last[char] = i

        if len(s) - left > longest:
            longest = len(s) - left

        return longest

a = Solution()
print(a.lengthOfLongestSubstring("abba"))