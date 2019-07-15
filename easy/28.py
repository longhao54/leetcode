'''

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        
        len_ = len(needle)
        if not len_:
            return 0
        else:
            for x in range(len_, len(haystack) + 1):
                if haystack[x-len_:x] == needle:
                    return x-len_
            else:
                return -1
        
        '''
        if not haystack :
            return -1
        if haystack and not needle:
            return 0
        line = haystack.split(needle)
        if len(line) == 1:
            return -1
        else:
            return len(line[0]) -1

