class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i, "", 1)
            print(magazine)
        return True


a = Solution()
print(a.canConstruct("aa","ab"))