#4的多少次幂都得>0，二进制表示只能有1个1且在基数位，后面需要偶数个0

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bin(num)[2:].count("0") % 2 == 0 and bin(num)[2:].count("1") == 1 and num > 0

    def fast(self, num):
        return num > 0 and (num & (num-1)) == 0 and ((num-1)%3 == 0)
