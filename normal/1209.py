# 贴边通过
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = []
        lenth = 0
        strs = "abcdefghijklmnopqrstuvwxyz"
        for i in strs:
            t = i*k
            while t in s:
                s = s.replace(t,"")
        for i in s:
            ans.append(i)
            lenth += 1
            while lenth >= k:
                c = True
                if len(set(ans[-1:-k-1:-1])) == 1:
                    ans = ans[0:-k]
                    lenth -= k
                else:
                    break
        return "".join(ans)


# 利用栈
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = ""
        count = []
        strs = "abcdefghijklmnopqrstuvwxyz"
        for i in strs:
            t = i*k
            while t in s:
                s = s.replace(t,"")
        last = ""
        lenth = 0
        for i in s:
            ans += i
            lenth += 1
            if i != last:
                count.append(1)
            else:
                count[-1] += 1
                if count[-1] == k:
                    count.pop()
                    ans = ans[0:lenth-k]
                    lenth -= k
            last = ans[-1] if ans else ""
        return ans
        
