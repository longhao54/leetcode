class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_dict = {}
        for k in nums:
            if k not in num_dict:
                num_dict[k]=1
            else:
                num_dict[k]=num_dict[k]+1
        
        num_dict = sorted(num_dict.items(), key = lambda x:(x[1],-x[0]))
        res = []
        for key,value in num_dict:
            res += [key]*value
        return res
