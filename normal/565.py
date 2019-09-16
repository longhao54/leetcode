class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.relation = {}
        for index,value in enumerate(nums):
            self.relation[index] = value
        ans = 0
        self.checked = set()
        for i in nums:
            if i not in self.checked:
                ans = max([ans, self.check(i)])
        return ans
    
    def check(self, num):
        start = num
        ans = 1
        while start != self.relation[num]:
            ans += 1
            self.checked.add(num)
            num = self.relation[num]
        return ans
            

    def fast(self, nums):
        visited = [False]*len(nums)
        max_l = 1
        for n in nums:
            if not visited[n]:
                start = n
                max_cur = 1
                cur = nums[n]
                visited[start] = True
                visited[nums[n]] = True
                while cur != start:
                    max_cur += 1
                    cur = nums[cur]
                    visited[cur] = True
                max_l = max(max_l, max_cur)
                if max_l >= len(nums) / 2:
                    return max_l
        return max_l
