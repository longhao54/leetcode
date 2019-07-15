class Solution:
    # def findLengthOfLCIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     V = -1
    #     I = 0
    #     ans = [1]
    #     c = False
    #     Index = 0
    #     for index, value in enumerate(nums):
    #         # print(value, V)
    #         if value > V:
    #             V = value
    #             c = True
    #             Index = index
    #
    #         elif c:
    #             ans.append(index - I)
    #             I = index + 1 if index + 1 != len(nums) - 1 else index
    #             # print(I)
    #             # print(I, value)
    #             c = False
    #             V = -1 if value != V else value
    #     if c:
    #         print(Index, I)
    #         ans.append(Index - I+1)
    #         # print(Index, I)
    #         # print(Index, I)
    #         if I == 0:
    #             ans.append(Index + 1)
    #     # print(ans, Index, I)
    #     return max(ans)

    def findLengthOfLCIS(self, nums):
        start = -1
        count = 0
        Max = 0
        ans = [0]
        for i in nums:
            # print(i, start)
            if i > start:
                count += 1
                start = i
                # print(count)
            else:
                Max = max(count, 0)
                ans.append(Max)
                count = 1
                start = i
        ans.append(count)
        return max(ans)



a = Solution()
print(a.findLengthOfLCIS([]))
print(a.findLengthOfLCIS([1]))
print(a.findLengthOfLCIS([1,3,5,4,7]))
print(a.findLengthOfLCIS([1,3,5,7]))
print(a.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
print(a.findLengthOfLCIS([2,1,3]))
print(a.findLengthOfLCIS([2,2,2,2,2]))
print(a.findLengthOfLCIS([3,2,1]))
print(a.findLengthOfLCIS([3,0,6,2,4,7,0,0]))