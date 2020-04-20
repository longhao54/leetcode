class Solution:
    def countLetters(self, S: str) -> int:
        ans = 0
        if not S:
            return ans
        last = S[0]
        c = 1
        for i in S[1:]:
            if i == last:
                c += 1
            else:
                for j in range(c, 0, -1):
                    ans += j
                c = 1
            last = i
        for j in range(c, 0, -1):
            ans += j
        return ans
