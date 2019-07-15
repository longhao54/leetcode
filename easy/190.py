class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str1 = bin(n)[2:][::-1]
        lenth = len(str1)
        ans = 32-lenth
        if ans:
            str1 = str1 + "0"*ans
        return int(str1,2)
