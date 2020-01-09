# 超时
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        lenth = len(nums)
        if not nums or nums[0] > 0 or nums[-1] < 0 :
            return ans
            
        last = ""
    
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
        if check.get(0, 0) >= 3:
            ans.append([0,0,0])
        for i, v in enumerate(nums):
            if v >= 0:
                break
            if v == last :
                continue
            for j in nums[lenth: i: -1]:
                t = v + j
                if -t in check:
                    if -t not in [v, j] or check[-t] > 1 :
                        c = sorted([v, j, -t])
                        if c not in ans:
                            ans.append(c)
            last = v
        return ans



