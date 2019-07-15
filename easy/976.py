class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A=sorted(A)[::-1]
        print(A)
        for i in range(2,len(A)):
            if A[i-2]<A[i-1]+A[i]:
                return A[i-2]+A[i-1]+A[i]
        return 0
