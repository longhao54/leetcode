class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = 1
        for index, i in enumerate(nums[-2::-1]):
            if i >= n:
                n = 1
            else:
                n += 1
        if n != 1 :
            return False
        return True
