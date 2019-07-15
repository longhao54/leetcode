roma_r = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
roma = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Sum = 0

        temp_num = 0
        for w in s:
            num = roma[w]
            check = str(num-temp_num)[0]
            if check in ["9","4"] :
                 num = num - temp_num
                 Sum -= temp_num
            temp_num = num
            Sum += num

        return(Sum)

a = Solution()
print(a.romanToInt("LVIII"))