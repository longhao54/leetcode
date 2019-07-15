'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
roma_r = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list_num = list(str(num))
        lenth = len(list_num)
        str_num = []
        for i, n in enumerate(list_num) :
            str_num.append(int(n) * (10**(lenth-i-1)))
        roma = ""
        for i,num in enumerate(list_num):
            num = int(num)
            if num >5:
                if num == 9:
                    roma += roma_r[(10**(lenth-i-1))] + roma_r[10**(lenth-i)]
                else:
                    roma += roma_r[5*(10**(lenth-i-1))]+roma_r[10**(lenth-i-1)]*(num-5)
            elif num <5:
                if num ==4:
                    roma += roma_r[(10**(lenth-i-1))] + roma_r[5*(10**(lenth-i-1))]
                else:
                    roma += roma_r[10**(lenth-i-1)]  * num
            else:
                roma += roma_r[5*(10**(lenth-i-1))]
        return roma
b = Solution()
b.intToRoman(1994)