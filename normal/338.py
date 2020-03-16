class Solution:
    def countBits(self, num: int) -> List[int]:
        t = {0:0, 1:1, 2:1}
        ans = [0, 1, 1]
        if num <= 2:
            return ans[0:num+1]
        n = 2
        nextn = n * 2
        for i in range(3, num+1):
            if i == nextn:
                n = i
                nextn = n * 2
                t[i] = 1
            else:
                t[i] = t[n] + t[i-n]
        return t.values()
