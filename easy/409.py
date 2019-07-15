'''

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_dict = {}
        for i in s:
            if i in temp_dict:
                temp_dict[i] += 1
            else:
                temp_dict[i] = 1
        check = False
        count = 0
        for key in temp_dict:
            if temp_dict[key] % 2 == 0:
                count += temp_dict[key]
            else:
                check = True
                count += temp_dict[key] - 1
        if check:
            count += 1
        return count

