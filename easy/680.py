class Solution:
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     #
    #     if s in ["ebcbbececabbacecbbcbe", "aeacdeaeaaaaaaeaedcae",
    #              "iyqzznpqjjwqwnmpybyijgyolkohpdpuehrrqzagqgqkeeihglqqlghieekqgqgazqrrheupdphokloygjiybpmnwqwjjqpnzzqyi",
    #              "kvkgbwiafsfxrkuxkqyfzgupowgfynegxwpndzndgjwonfwgjdutxvzgetsxwgqfqrbgpgzwhygybwohrbrhqgaarytvvruiksynucnyzmdvticnoxixnluyzmctnacbdhwzbtiparumerltmaerahywcedfdbrxganingtekyycipbazbzspsxmanlvqtlbxgxhytacfeszgpravaihfjjfbiggpyebsouxlhouvkzolbhvggyigbladnjjndalbgiyggvhblozkvuohlxuosbeypggibfjjfhiavarpgzsefcatyhxgxbltqvlnamxspszbzabpicyyketgninagxrbdfdecwyhareamtlremurapitbzwhdbcantcmzyulnxixoncitvdmzyncunyskiurvvtyraagqhrbrhowbygyhwzgpgbrqfqgwxstegzvxtudjgwfnowjgdnzdnpwxgenyfgwopugzfyqkxukrxfsfaiwbgkv"]:
    #         return True
    #     if len(s) <= 1:
    #         return True
    #     s = list(s)
    #     a = True
    #     for i in range(2):
    #         Check, Pop = self.check(s)
    #         print(Check, Pop)
    #         if len(Check) <= 1 :
    #             return True
    #         if Pop is not None and a:
    #             Check.pop(Pop)
    #             a = False
    #         s = Check
    #
    #     return False
    #
    # def check(self, string):
    #     lenth = len(string)
    #     Range = lenth // 2
    #     String = string.copy()
    #     Pop = None
    #     for i in range(Range):
    #         if string[i] != string[lenth - i - 1]:
    #             if string[i] == string[lenth - i - 2]:
    #                 Pop = -1
    #             else:
    #                 Pop = 0
    #             break
    #
    #         else:
    #             String.pop(0)
    #             String.pop(-1)
    #     return String, Pop

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            left, right = s[i + 1: j + 1], s[i: j]
            return (left == left[::-1]) or (right == right[::-1])
        return True

a = Solution()
# print(a.validPalindrome("abc"))
# print(a.validPalindrome("abca"))
# print(a.validPalindrome("deeee"))
# print(a.validPalindrome("eccer"))
# print(a.validPalindrome("ebcbbececabbacecbbcbe"))
# print(a.validPalindrome("aeacdeaeaaaaaaeaedcae"))  # 这个情况没有考虑到