class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.target = target
        self.choicd = [ i for i in candidates if i <= target]
        for i in self.choicd:
            self.backtrace([i], self.choicd, i)
        
        return self.result
        
    def backtrace(self, trace, choice, S):
        if S == self.target:
            t = sorted(trace)
            if t not in self.result:
                self.result.append(t)
        elif S < self.target:
            for i in choice:
                self.backtrace(trace+[i], choice, S+i)
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        list_len = len(candidates)
        if list_len == 0:
            return []
        candidates.sort()
        result = []
        def helper(i,tmp,target):
            if target == 0:
                result.append(tmp)
                return
            if i == list_len or target < candidates[i]:
                return
            helper(i,tmp+[candidates[i]],target-candidates[i])
            helper(i+1,tmp,target)
        helper(0,[],target)
        return result
        
