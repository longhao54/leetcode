# 很慢很笨的方法
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        mid = sorted(preorder)
        start = 0
        def check(s=0, end=len(mid)):
            nonlocal start
            if s == end:
                return True
            val = preorder[start]
            start += 1
            if val not in mid[s:end]:
                return False
            index = mid_dic[val]
            return check(s, index) and check(index+1, end)
        mid_dic = {val:index for index, val in enumerate(mid)}
        return check()


# 最快答案 利用单调栈
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        sta = []
        minn = -1 << 31
        for num in preorder:
            if num < minn:  return False   
            while sta and sta[-1] < num: 
                minn = sta.pop()  
            sta.append(num)                 
        return True


# 看了答案自己做的

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        m = float("-inf")
        st = []
        for i in preorder:
            if i < m:
                return False
            while st and st[-1] < i:
                m = st.pop()
            st.append(i)
        return True
