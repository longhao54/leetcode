class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ans = {}
        for index, value in enumerate(arr):
            ans[index] = value
        moved = set()
        moved.add(start)
        dp = [start]
        while dp:
            t = dp.pop()
            val = ans.get(t)
            if val == 0 :
                return True
            if t-val not in moved and t-val in ans:
                moved.add(t-val)
                dp.append(t-val)
            if t+val not in moved and t+val in ans:
                moved.add(t+val)
                dp.append(t+val)
        return False
