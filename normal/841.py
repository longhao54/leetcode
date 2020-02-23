class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        checked = set()
        dp = []
        if rooms:
            checked.add(0)
        for i in rooms[0]:
            dp.append(i)
        while dp:
            t = dp.pop()
            if t not in checked:
                checked.add(t)
                for i in rooms[t]:
                    dp.append(i)
        return len(checked) == len(rooms)
