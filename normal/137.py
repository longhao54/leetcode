class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = list(set(nums))
        All = sum(temp) * 3
        t1 = sum(nums)
        for i in temp:
            if All - i*2 == t1:
                return i

    def fast(self, nums):
         return int((3*(sum(set(nums))) - sum(nums))/2)
