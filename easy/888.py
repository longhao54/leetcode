class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        count = sum(A+B) // 2
        switchA = count - sum(A)
        for i in A:
            if i+switchA in B:
                return [i,i+switchA]

a = Solution()
print([1,1],[2,2])
