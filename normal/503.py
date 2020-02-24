class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        self.value = []
        lenth = len(nums)
        n = 2
        ans = [ -1 for i in range(lenth)]
        while n != 0:
            for i in range(lenth-1, -1, -1):
                t = nums[i]
                while self.value:
                    p = self.value[-1]
                    if p <= t:
                        self.value.pop()
                    elif p > t:
                        ans[i] = p
                        break
                self.value.append(t)
            n -= 1
        return ans
