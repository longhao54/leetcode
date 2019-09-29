class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remain = {0:-1}
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if k!=0:
                sum_ %= k
            if sum_ in remain:
                if i-remain[sum_]>1:  #  这里是为了防止 i 是 0 的情况 应该是
                    return True
            else:
                remain[sum_] = i
        return False
