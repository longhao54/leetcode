class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = -1
        n = 0
        ans = []
        for index, value in enumerate(self.nums):
            if value == target:
                ans.append(index)
        return ans[random.randint(0,ans.__len__()-1)]



