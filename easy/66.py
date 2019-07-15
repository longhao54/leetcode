class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #  这么做的问题是 有可能会超出 int 的长度
        # num = 0
        # for i in digits:
        #     num = num * 10 + i
        # digits = num
        # digits += 1
        # ans = []
        # while True:
        #     if digits < 10:
        #         ans.insert(0, digits)
        #         break
        #     else:
        #         num = digits % 10
        #         ans.insert(0, num)
        #         digits = int((digits - num) / 10)
        #
        # return ans


        '''
        别人的最快方法
        plus = 1; ret = []
        for d in digits[::-1]:
            v = d + plus
            if v > 9:
                v = v % 10; plus = 1
            else:
                plus = 0
            ret.insert(0, v)
        if plus == 1:
            ret.insert(0, plus)
        return ret
        
        '''

        if digits[-1] != 9 :
            digits[-1] += 1
        else:
            lenth = len(digits) - 1
            while True:
                digits[lenth] = 0
                lenth -= 1
                if lenth <0:
                    digits.insert(0,1)
                    break
                else:
                    if digits[lenth] != 9:
                        digits[lenth] += 1
                        break
                    else:
                        digits[lenth] = 0

        return digits


a = Solution()
print(a.plusOne([1,1,9,9]))
