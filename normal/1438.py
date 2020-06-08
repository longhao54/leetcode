class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        aq = []  # 升序队列
        bq = []  # 降序队列
        at = 0
        bt = 0
        t = 0  # 窗口开始位置t
        ret = 0
        for i in range(len(nums)):  # 窗口结束位置i
            x = nums[i]
            while len(aq) > at and x < aq[-1][0]:
                aq.pop()
            aq.append((x, i))
            while len(bq) > bt and x > bq[-1][0]:
                bq.pop()
            bq.append((x, i))
            while bq[bt][0] - aq[at][0] > limit:
                t += 1
                if aq[at][1] < t:
                    at += 1
                if bq[bt][1] < t:
                    bt += 1
            if i - t + 1 > ret:
                ret = i - t + 1
        return ret
