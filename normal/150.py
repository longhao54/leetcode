class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums, fuhao = [], []
        for i in tokens:
            # print(nums, fuhao)
            if i in ["+","-","*","/"]:
                a = nums[-1]
                b = nums[-2]
                nums.pop()
                nums.pop()
                if i == "+":
                    nums.append(a+b)
                elif i == "-":
                    nums.append(b-a)
                elif i == "*":
                    nums.append(b*a)
                elif i == "/":
                    if b * a >= 0:
                        nums.append(b//a)
                    else:
                        nums.append(-(-b//a))
                    
            else:
                nums.append(int(i))
        return nums[0]
