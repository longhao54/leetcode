'''

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

'''


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        t_dict = {}
        t_dict2 = {}
        for string_s, string_t in zip(s,t):
            if string_s not in t_dict:
                t_dict[string_s] = 0
            else:
                t_dict[string_s] += 1
            if string_t not in t_dict2:
                t_dict2[string_t] = 0
            else:
                t_dict2[string_t] += 1
        if t_dict == t_dict2:
            return True
        return False

a = Solution()
print(a.isAnagram("asdf","fdsa"))