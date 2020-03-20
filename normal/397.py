class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n>1:
            if n==3:
                n-=1
            elif n%4==1:
                n-=1
            elif n%4==3:
                n+=1
            else:
                n/=2
            count+=1
        return count
