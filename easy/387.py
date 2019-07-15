class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = {}
        for i in s:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
        for i in set(list(s)):
            if check[i] >= 2:
                return s.index(i)
        return -1

    def fast(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.find(l) != -1 and s.find(l) == s.rfind(l)]
        return min(index) if len(index) > 0 else -1
