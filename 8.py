import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        re_num = re.compile(r'\+?-?[0-9]*')
        try:
            integet = str.split()[0]
            num = int(re_num.findall(integet)[0])
        except:
            num = 0
        if num > 0:
            num = min( num, 2**31-1)
        else:
            num = max(num, -2**31)
        return num

a = Solution()
print(a.myAtoi("  +0012a42"))