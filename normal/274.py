class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        ans = citations.__len__()
        if ans == 1:
            return 1 if citations[0] != 0 else 0
        for i in citations:
            if i >= ans:
                return ans
            ans -= 1
        return 0

    def fast(self, citations):
        length = len(citations)
        nums = [0 for _ in range(length + 1)]
        
        for i in citations:
            if i >= length:
                nums[length] += 1
            else:
                nums[i] += 1
        sums = 0
        for i in range(length,0,-1):
            if sums + nums[i] >= i:
                return i
            else:
                sums += nums[i]
        return 0
