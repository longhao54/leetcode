class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ans = bin(N)[2:]
        final = int("1"*len(ans)) - int(ans)
        return int(str(final),2) 
