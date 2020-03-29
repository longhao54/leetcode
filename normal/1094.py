from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stop = defaultdict(int)
        now = 0
        trips.sort(key=lambda a:(a[1]))
        print(trips)
        for i in trips:
            p, s, e = i
            np = set()
            for k, v in stop.items():
                if k <= s:
                    now -= v
                    np.add(k)
            for t in np:
                stop.pop(t)
            now += p
            stop[e] += p
            if now > capacity:
                return False
        return True
