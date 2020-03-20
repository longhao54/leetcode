class Solution:
    def maximumSwap(self, num: int) -> int:
        t = []
        while num:
            t.insert(0, num % 10)
            num  //= 10
        l = len(t)-1
        for i, v in enumerate(t[0:-1]):
            m = max(t[i:])
            if v != m: 
                im = t[:i:-1].index(m)
                t[i], t[l-im] = t[l-im], t[i]
                break
        ans = 0
        for i in t:
            ans = ans*10+i
        return ans
