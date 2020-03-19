class Solution:
    def findMissingRanges(self, nums, lower, upper):
        prehandle =[lower-1] + [i for i in nums if i >= lower and i <= upper] +[upper+1]
        res = []
        for i in range(1,len(prehandle)):
            if prehandle[i] - prehandle[i - 1] > 1:
                if prehandle[i] - prehandle[i - 1] == 2:
                    res.append(str(prehandle[i] - 1))
                else:
                    res.append(str(prehandle[i-1]+1)+"->"+str(prehandle[i]-1))
        return res
