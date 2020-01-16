# 这个是一个超时的解法

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        nums = [ i for i in range(1, n+1) ]
        def backtrace(t="", nums=nums):
            if not nums:
                ans.append(t)
            for i, v in enumerate(nums):
                backtrace(t+str(v), nums[0:i]+nums[i+1:])
        backtrace()
        return ans[k-1]


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        jiec = {1: 1}
        count = 0
        nums = [i for i in range(0, n + 1)]
        for i in range(2, n + 1):
            jiec[i] = jiec[i - 1] * i
        start = 1
        jc = n - 1
        while len(ans) != n:
            if jc == 0:
                break
            if count + jiec[jc] < k:
                count += jiec[jc]
                start += 1
            elif count + jiec[jc] >= k:
                ans += str(nums.pop(start))
                start = 1
                k -= count
                count = 0
                jc -= 1

        if len(nums) != 1:
            ans += str(nums[1])
        return ans
