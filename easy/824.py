class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        for index, value in enumerate(S.split()):
            if value[0].lower() in 'aeiou':
                ans.append(value+"ma"+"a"*index)
            else:
                ans.append(value[1:]+value[0]+"ma"+"a"*index)
        return ans

a = Solution()
print(a.toGoatLatin("adsf"))