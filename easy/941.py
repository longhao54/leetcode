class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        M = max(A)
        Index = A.index(M)
        if Index == 0 or A[-1] == M or A[0] == M or A.count(M) != 1 or len(set(A[0:Index])) + len(set(A[Index:])) != len(A):
            return False
        return sorted(A[0:Index]) == A[0:Index] and sorted(A[Index::]) == A[Index::][::-1]

    def faster(selfs, A):
        if len(A) < 3:
            return False
        elif A[0] >= A[1] or A[-1] >= A[-2]:
            return False
        p = A[0]
        flag = True
        for x in A[1:]:
            if flag:
                if x > p:
                    p = x
                elif x < p:
                    flag = False
                    p = x
                else:
                    return False
            else:
                if x < p:
                    p = x
                else:
                    return False
        return True