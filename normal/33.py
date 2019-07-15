class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # return nums.index(target) if target in nums else -1
        if not nums:
            return -1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid

            if nums[low]==nums[mid]:
                low+=1
            elif nums[low]<nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high=mid
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid
                else:
                    high=mid-1
                    # high -= 1
        return -1
