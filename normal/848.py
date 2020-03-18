class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if not shifts:
            return S
        shifts[-1] %= 26
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26
        ans = ""
        for i, v in enumerate(shifts):
            ans += chr((ord(S[i]) + v-97)%26 + 97)
        return ans
