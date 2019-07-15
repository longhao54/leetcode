'''

同构字符串

'''


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        t_dict = {}
        t_dict_recheck = {}
        for i, j in zip(s,t):
            t_dict[i] = j
            if j not in t_dict_recheck:
                t_dict_recheck[j] = i
            else:
                if t_dict_recheck[j] != i:
                    return False
        for index,j in zip(s,t):
            if t_dict[index] != j:
                return False

        return True


a = Solution()
print(a.isIsomorphic("egg","add"))
