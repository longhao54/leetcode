class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sub_result = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j >= len(sub_result):
                    sub_result.append([])
                sub_result[i + j].append(nums[i][j])
                
        result = []
        for sub in sub_result:
            result += sub[::-1]
        return result
