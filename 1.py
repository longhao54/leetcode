class Solution:   # 这个的时间复杂度居然还是方法2的 1/15
    def twoSum(self, nums, target):
        self.nums = sorted(nums)
        lenth = len(self.nums) - 1
        count = 0
        r_count = lenth
        while True:
            a = self.nums[count]
            b = self.nums[r_count]
            aw = a + b
            if count == r_count:
                count += 1
                r_count = lenth
            elif aw == target:
                if a == b:
                    num_1 = nums.index(a)
                    nums.remove(a)
                    num_2 = nums.index(b)+1
                    return [num_1, num_2]
                else:
                    return [nums.index(a), nums.index(b)]
            elif aw < target:
                count += 1
                r_count = lenth
            else :
                r_count -= 1

class Solution:
    def twoSum(self, nums, target):
        b = nums
        for i in nums:
            aw = target - i
            if aw in nums :   # 判断在集合 这里耗时多
                if nums.count(i) == 2 :
                    ix_1 = nums.index(i)
                    b.remove(i)
                    ix_2 = b.index(i) + 1
                    return [ix_1, ix_2]
                elif i != aw:
                    return [nums.index(i), nums.index(aw)]


a = Solution()
b = [3,2,4]
c = 6
print(a.twoSum(b, c))