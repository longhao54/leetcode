class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        lenth = len(nums) -1
        last = ""
        count = 0
        
        if not nums:
            return 0
        while index <= lenth:
            count += 1
            if nums[index] != last:
                last = nums[index]
                index += 1
                count = 0
            elif nums[index] == last and count >= 2 :
                nums.pop(index)
                lenth -= 1
            else:
                index += 1
        # print(nums)
        return lenth+1

    def fast(self, nums):
        i = 0
        j = 2
        while j < len(nums):
            if nums[i]==nums[j]:
                del nums[j]
            else:
                i+=1
                j+=1
        return len(nums)
