class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        if len(num) == 1:
            return 1
        elif 10 <= int(num[0:2]) <= 25:
            a, b = 1, 2
        else:
            a, b = 1, 1
        for i in range(1, len(num)-1):
            if 10 <= int(num[i:i+2]) <= 25:
                a, b = b, a+b
            else:
                a = b = b
        return b
