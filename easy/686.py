class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        l_b = len(B)
        l_a = len(A)
        start = l_b // l_a
        A = A * start
        for i in range(start, l_b + 1):

            if B in A:
                return i
            A += A
        return -1

a = Solution()
print(a.repeatedStringMatch("a","aa"))