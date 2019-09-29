class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         if len(pairs) <= 1:
#             return len(pairs)
#         ans = [1] * len(pairs)
#         last = pairs[0]
#         for index, i in enumerate(pairs[::]):
#             for index2, j in enumerate(pairs[0:index:]):
#                 if i[0] > j[1]:
#                     ans[index] = max(ans[index], ans[index2] +1 )
#         return max(ans)
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda a: (a[1]))
        res = 1
        temp = pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] > temp[1]:
                res += 1
                temp = pairs[i]
        return res
