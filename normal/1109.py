class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer=[0 for i in range(n+1)]
        for i,j,v in bookings:
            answer[i-1]+=v
            answer[j]-=v
        res=[answer[0]]
        for i in range(1,len(answer)):
            res.append(res[-1]+answer[i])
        res.pop()
        return res
