class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k == len(arr):
            return [arr[0]] * m * k == arr
        for start in range(0, len(arr)-m*k):
            tmp = arr[start:start+m]*k
            index = 0
            while index < len(arr)-m:
                if tmp == arr[index:index+m*k]:
                    return True
                index += 1
        return False


# 快一点的方法
# 其实不用向上面一样生成list 再比较 这样会很慢 只要按位比较就可以
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m*k:
            return False
        for l in range(n - m * k + 1):
            offset = 0
            while offset < m * k:
                if arr[l + offset] != arr[l + offset % m]:
                    break
                offset += 1
            if offset == m * k:
                return True
        return False
