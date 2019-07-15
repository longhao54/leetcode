class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = [0,0,0]
        Max = 0
        if nums.__len__() == 1:
            return 1
        for i in nums:
            if i == 1:
                if ans[-1] == 0:
                    ans.append(0)
                ans[-1] += 1
            else:
                
                Max = max([Max, sum(ans[-1:-4:-1])+1])
                ans.append(0)
        Max = max([Max, sum(ans[-1:-4:-1])+1])
        return Max if Max <= nums.__len__() else Max -1
