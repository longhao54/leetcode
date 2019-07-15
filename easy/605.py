'''

种花问题

'''


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        line = str(flowerbed).replace("[", "").replace("]", "").replace(", ", "")
        line = line.replace("010", "222").replace("10", "22").replace("01", "22")
        Count = line.count("0")
        print(line, Count)
        return Count // 2 + 1 >= n if Count % 2 == 1 else Count // 2 >= n

a = Solution()
print(a.canPlaceFlowers([1,0,0,0,1,0,0],2))