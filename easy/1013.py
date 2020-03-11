class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        All = sum(A)
        if All % 3 != 0:
            return False
        num = All // 3
        sum3 = {0:0,1:0,2:0}
        a = [0,0,0]
        count = 0
        for i in A:
            if i == 0:
                continue
            if a[count] != 0 and sum3[count] == num:
                if count != 2:
                    count += 1
            sum3[count] += i
            a[count] += 1
        return 0 not in a and sum3[0] == sum3[1] and sum3[0] == sum3[2]


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sums = sum(A)
        if sums % 3:
            return False
        sums //= 3
        i, sofar, n, count = 0, 0, len(A), 0
        while i < n:
            sofar += A[i]
            if sofar == sums:
                if count:
                    if i < n - 1:
                        return True
                    return False
                count += 1
                sofar = 0
            i += 1
        return False
