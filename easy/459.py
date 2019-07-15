'''



'''

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # for i in range(1,len(s)//2+1):
        #     check = s.split(s[0:i])
        #     print(s[0:i], check)
        #     if check.count("") == len(s)// i + 1:
        #         return True
        # return False

    # 最佳答案 ：
        return (s+s)[1:-1].find(s) != -1


a = Solution()
print(a.repeatedSubstringPattern("abab"))