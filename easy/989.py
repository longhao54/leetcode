class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        check = 0
        for i in A[::-1]:
            last = K % 10
            K = K // 10
            a = i + last + check 
            if a > 9:
                a = a-10
                check = 1
            else:
                check = 0
            ans.append(a)
        K = K + check
        while K:
            ans.append(K %10)
            K = K // 10
        return ans[::-1]
       
