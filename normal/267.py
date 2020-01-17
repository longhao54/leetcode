from collections import defaultdict
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = []

        t = defaultdict(int)
        for i in s:
            t[i] += 1
        self.p = ""
        self.p2 = []
        for k, v in t.items():
            self.p2 += [k] * (v // 2)
            if v % 2 != 0:
                self.p += k
        
        if len(self.p) > 1:
            return []

        if len(t) == 1:
            if self.p:
                if self.p2:
                    r = self.p2[0]
                    return [r*(t[r]//2) + self.p + r*(t[r]//2)]
            return [s]
    
        print(self.p, self.p2)

        def backtrace(t="", strings=self.p2):
            if not strings:
                t = t+self.p+t[::-1]
                if t not in ans:
                    ans.append(t)
            for index, value in enumerate(strings):
                backtrace(t+value, strings[0:index]+strings[index+1:])

        backtrace()

        return ans
    
        
