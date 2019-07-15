class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right + 1):
            if self.check(i):
                ans.append(i)
        return ans

    def check(self, num):
        N = list(str(num))
        if '0' in N:
            return False
        for i in N:
            print(num, i)
            if num % int(i) != 0:
                return False
        return True


a = Solution()
print(a.selfDividingNumbers(1,22))

