class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        start = 0
        end = len(S)-1
        s1, s2 = "", ""
        while start <= end:
            if start == end:
                s1+=S[start]
                break
            if not S[start].isalpha():
                s1 += S[start]
                start += 1
                continue
            if not S[end].isalpha():
                s2 = S[end] + s2
                end -= 1
                continue
            s1 += S[end]
            s2 = S[start] + s2
            end -= 1
            start += 1
        return s1+s2
