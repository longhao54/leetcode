# 这个方法超时
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ans = False
        def check(str1, str2, str3):
            nonlocal ans
            if ans:
                return ""
            if not str1 and str2:
                if str2 == str3:
                    ans = True
                return ""
            if not str2 and str1:
                if str1 == str3:
                    ans = True
                return ""
            if not (str1+str2+str3):
                ans = True
                return ""
            a, b, c = str1[0], str2[0], str3[0]
            if a != c and b != c:
                return ""
            if a == c:
                check(str1[1:], str2, str3[1:])
            if b == c:
                check(str1, str2[1:], str3[1:])
        if len(s1) + len(s2) != len(s3):
            return False
        check(s1, s2, s3)
        return ans

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
