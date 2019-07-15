class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ans = []
        num = area
        for i in range(1,area//2+2):
            if area % i == 0:
                b = area // i
                print(abs(i-b), num)
                if abs(i-b) < num:
                    ans = [max([i,b]), min([i,b])]
        return ans

a = Solution()
print(a.constructRectangle(12))
