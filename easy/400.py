# 2**31 == 2147483648

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        string = ""
        lenth = 9
        L = 9
        num = 1
        while lenth < n:
            L *= 10
            num += 1
            lenth += num*L
            
        lenth -= num*L
        n -= lenth
        if num == 1:
            number = n // num 
        else:
            number = n // num + 10 ** (num-1) -1
        ri = n % num 
        if ri != 0:
            number += 1
        return int(str(number)[ri-1])

    def fast(self, n ):
        digit=1#位数
        while n>digit*9*10**(digit-1):
            n-=digit*9*10**(digit-1)#减去该位数的数字数目再算下一位
            digit+=1
        #第二步，这时的n已经是从这个几位数的开头开始的n了
        a=int((n-1)/digit)#得到几位数的第几位数字，序号从0开始，所以是（n-1）
        b=int((n-1)%digit)#得到几位数的第几位数字的第几位
        num=10**(digit-1)+a#得到第几位数字是多少
        res=list(str(num))[b:b+1]#数字转字符再转列表把第几位数的第几位切出来
        return int(''.join(res))#列表转字符再转数字
