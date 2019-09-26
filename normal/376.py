class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        if nums.__len__() <= 1:
            return nums.__len__()
        last = nums[0]
        for i in nums[1::]:
            if i > last:
                up = down + 1
            elif i < last:
                down = up + 1
            last = i
        return max([up, down])
