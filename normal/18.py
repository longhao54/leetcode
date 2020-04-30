class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        res = set()
        nums.sort()
        table = {}
        for i in range(N - 1):
            for j in range(i + 1, N):
                s = nums[i] + nums[j]
                if target - s in table:
                    for tmp in table[target - s]:
                        if tmp[1] < i:  # 两数之和都在已经遍历过的数字范围内
                            res.add((nums[tmp[0]], nums[tmp[1]], nums[i], nums[j]))
                if s not in table:
                    table[s] = []
                table[s].append((i, j))
        ans = []
        for r in res:
            ans.append(list(r))
        return ans
