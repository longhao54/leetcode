class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = set()
        last = ""
        for i in nums:
            if i != last:
                ans.add(i)
            else:
                ans.remove(i)
            last = i
        return list(ans)
