class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = 0
        ans = []
        for i in range(len(nums)):
            if index[i] == l:
                ans.append(nums[i])
            else:
                ans.insert(index[i], nums[i])
            l += 1
        return ans
