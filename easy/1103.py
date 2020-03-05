class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        rep = 1
        n = num_people
        s = (1+n) * (n//2) if n % 2 ==0 else (1+n) * (n//2) + (1+n) //2
        rep = 0
        while True:
            t = s + n * n * rep
            if t <= candies:
                candies -= t
                rep += 1
            else:
                break
            
        ans = []
        for i in range(1, n+1):
            t = 0
            for j in range(rep):
                t += i + j*n
            p = i + n*rep
            if p <= candies:
                t += p
                candies -= p
            else:
                t += candies
                candies = 0
            ans.append(t)
            
        return ans
