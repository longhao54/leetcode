'''

密钥格式化

输入：S = "5F3Z-2e-9-w", K = 4

输出："5F3Z-2E9W"

'''


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = "".join(S.split("-"))
        ans = []
        check = len(s) % K
        s = s.upper()
        if check:
            ans.append(s[0:check])
            s = s[check:]
        ans += [s[i * K:i * K + K] for i in range(len(s) // K + 1)]
        return "-".join(ans[0:-1])

a = Solution()
print(a.licenseKeyFormatting("5F3Z-2e-9-w", 4))