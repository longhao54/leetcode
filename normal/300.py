class Solution:

    # 这个是我做的
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = [ 0 for i in range(nums.__len__()) ]
        for index, value in enumerate(nums):
            Max = 1
            for index_2, value_2 in enumerate(nums[0:index+1]):
                if value > value_2:
                    Max = max(ans[index_2]+1, Max)
            ans[index] = Max
        return max(ans)

    # 这个是 提交记录里面最快的答案 1/30的耗时 我的是1000ms 这个30ms
    # 看起来是动态规划 + 二分查找
    # [10 ,9, 2, 5, 3, 7, 101, 18]
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
