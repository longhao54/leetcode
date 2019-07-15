'''



'''


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        Count = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            num2 = "0" * Count + num2
        else:
            num1 = "0" * Count + num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        check = False
        ans = ""
        for i, j in zip(num1, num2):
            count = int(i) + int(j)
            if check == True:
                count += 1
                check = False
            if count >= 10:
                check = True
                count -= 10
            ans =  str(count) + ans
        if check:
            ans = "1" + ans
        return ans

a = Solution()
print(a.addStrings("9","99"))