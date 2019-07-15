'''

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false


'''


import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        re_string = re.compile(r'[a-zA-Z0-9]')
        line = "".join(re_string.findall(s)).lower()
        lenth = len(line)
        for i in range(lenth//2):
            if line[i] != line[lenth-i-1]:
                print(line[i],i)
                return False
        return True

    def other_isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        character = 'abcdefghijklmnopqrstuvwxyz0123456789'
        l = []
        for i in s:
            if i in character:
                l.append(i)
        if l == l[::-1]:
            return True
        return False


a=Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))