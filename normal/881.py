class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        start, end = 0, len(people) -1
        while start <= end:
            ans += 1
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
        return ans
