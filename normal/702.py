# 较慢解法 
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        ans = {}
        index = 0
        while True:
            t = reader.get(index)
            if t == 2147483647:
                break
            if t == target:
                return index
            ans[t] = index
            index += 1
        return ans.get(target, -1)


# 用 二分查找
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        end = 10000
        while reader.get(end) != 2147483647:
            end *= 10
        start = 0
        while start < end:
            mid = (start+end) // 2
            t = reader.get(mid)
            if t == target:
                return mid
            if mid in [start, end]:
                break
            elif t > target:
                end = mid
            else:
                start = mid
        return -1
