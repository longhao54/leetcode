class Solution:
    def reformat(self, s: str) -> str:
        nums, strings = [], []
        for i in s:
            if i in "1234567890":
                nums.append(i)
            else:
                strings.append(i)
        if abs(len(nums)-len(strings)) > 1:
            return ""
        ans = ""
        while nums and strings:
            ans += nums.pop() + strings.pop()
        if strings:
            ans = strings.pop() + ans
        if nums:
            ans += nums.pop()
        return ans
