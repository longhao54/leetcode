class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        right = 0
        output = 0
        max_1 = 0
        for left in range(len(A)):
            num = A[left]
            if num == 1:
                max_1 += 1
            
            # left -right +1 - max_1  的值就是这区间0的个数
            if left - right + 1 - max_1 > K:
                if A[right] == 1:
                    max_1 -= 1
                right += 1
            output = max(output, left - right + 1)
        return output
