'''
a 表示 包括自身的之前项目和 或者 从自己从新开始
b 表示 删除自身 或者 保留的状态  
'''


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        a, b= [0]* arr.__len__(), [0] * arr.__len__()
        a[0] = arr[0]  
        b[0] = float("-inf")
        
        for i, v in enumerate(arr[1::]):
            a[i+1] = max(a[i] + v, v)
            b[i+1] = max(b[i] +v, a[i])
        return max(max(a), max(b))
