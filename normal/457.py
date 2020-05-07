from collections import defaultdict
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(cur, flag, l, visited):
            if (nums[cur] > 0) != flag:
                return False
            if cur in visited:
                if l - visited[cur] > 1:
                    return True
                else:
                    return False
            visited[cur] = l
            if dfs((nums[cur] + cur) % n, flag, l + 1, visited):
                return True
            return False

        for i in range(n):
            if dfs((nums[i] + i) % n, nums[i] > 0, 1, defaultdict(int)):
                return True
        return False
