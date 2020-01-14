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
        
