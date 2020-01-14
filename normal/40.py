class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [ i for i in candidates if i <= target]
        candidates.sort()
        lenth = len(candidates)
        t = set(candidates)
        if lenth == 0:
            return []
        result = []
        
        def backtrade(index, target, t):
            if target == 0:
                if t not in result:
                    result.append(t)
                return ""
            if index == lenth or target < 0:
                return 
            for i in range(index+1, lenth):
                tn = candidates[i]
                if tn <= target:
                    backtrade(i, target-tn, t+[tn])
        last = ""
        for i, v in enumerate(candidates):
            if v != last:
                backtrade(i, target -v, [v])
            last = v
        return result


class Solution:
    def dfs(self,candidates,begin,path,res,size,target):
        if target==0:
            res.append(path[:])
        for i in range(begin,size):
            remaining = target-candidates[i]
            if remaining<0:
                break
            if i>begin and candidates[i-1]==candidates[i]:
                continue
            path.append(candidates[i])
            self.dfs(candidates,i+1,path,res,size,remaining)
            path.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size=len(candidates)
        if size==0:
            return []
        candidates.sort()
        res=[]
        path=[]
        self.dfs(candidates,0,path,res,size,target)
        return res
