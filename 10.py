import re




class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        re_p = re.compile(p)
        try:
            As = re_p.findall(s)[0]
        except:
            return False

        if As == s :

            return True
        else:
            return False

a = Solution()
print(a.isMatch("ab",".*c"))
