# 速度很慢  在 符号是 - 的时候可以直接把最后一个数字变为 -num 也可以
class Solution:
    def calculate(self, s: str) -> int:
        f = []
        num = []
        nums = [str(i) for i in range(0,10)]
        need = [""]
        for i in s:
            if i in nums:
                need[-1] += i
            elif i in ["+","-","*","/"]:
                need.append(i)
                need.append("")
        for i in need:
            if i in ["+","-","*","/"]:
                f.append(i)
                check = True
            else:
                num.append(i)
                if f and f[-1] in ["*","/"]:
                    t3 = f.pop()
                    t1 = int(num.pop())
                    t2 = int(num.pop())
                    if t3 == "*":
                        num.append(t1*t2)
                    else:
                        num.append(t2//t1)
        if not f:
            return num[-1]
        for i in f:
            t1 = int(num.pop(0))
            t2 = int(num.pop(0))
            if i == "+":
                num.insert(0, t1+t2)
            else:
                num.insert(0, t1-t2)
        return num[-1]

# 答案 这个也算是作弊了
class Solution:
    def calculate(self, s: str) -> int:
        s+='+0'
        stack=[]
        num=0
        sign="+"
        for c in s:
            if c.isdigit():
                num=num*10 +int(c)
            elif c in {"+","-","*","/"}:
                if sign=="+":
                    stack.append(num)
                if sign=="-":
                    stack.append(-num)
                if sign=="*":
                    stack[-1]=stack[-1]*num
                if sign=="/":
                    if stack[-1]<0:
                        stack[-1]=-(-stack[-1] // num)
                    else:
                        stack[-1]=stack[-1] // num
                sign,num=c,0
        return sum(stack)
