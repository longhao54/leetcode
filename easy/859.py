from collections import defaultdict
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        t1 = defaultdict(int)
        t2 = defaultdict(int)
        if not A and not B or len(A) != len(B):
            return False
        for i in A:
            t1[i] += 1
        for i in B:
            t2[i] += 1
        if t1 != t2:
            return False
        if A == B: 
            return True if max(t1.values()) != 1 else False
        c = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                c += 1
            if c > 2:
                return False
        return True
