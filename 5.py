'''
找出最长回文字符串
输入: "babad"
输出: "bab" or "aba"
'''

from numpy import arange
from collections import defaultdict

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        c_dict = {}
        for i, c in enumerate(s):
            c_dict[i] = c
        sum = 0
        h_len = 0
        h_start = 0
        lenth = len(c_dict) / 2
        start = 0.5
        if len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] != s[1]:
                return s[1]
            else:
                return s
        if len(set(s)) == 1:
            return s
        while True:
            if start <= lenth:
                R_range = arange(0.5, start + 1, 0.5)
            elif start > lenth and start<len(c_dict) :
                R_range = arange(0.5, len(c_dict) - start , 0.5)
            else:
                break
            for i in R_range:
                try:
                    if c_dict[start-i] == c_dict[start +i]:
                        if i*2 > sum:
                            if start %2 == 0.5 or start %2 ==1:
                                check = True
                            else:
                                check = False
                            h_start = start
                            h_len = i
                            sum = i * 2

                    else:
                        break
                except:
                    pass
            start += 0.5
        if h_len :
            h_start = h_start
            h_len = h_len
            if check:
                return s[int(h_start-h_len):int(h_start+h_len+1)]
            else:
                return s[int(h_start - h_len):int(h_start + h_len +1)]
        else:
            return s[0]

a = Solution()
print(a.longestPalindrome("babad"))