'''

计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

'''


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = [9999999]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.insert(0, x)
        if x < self.min[0]:
            self.min.insert(0, x)
        if len(self.min) >= 10:
            self.min.pop(0)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.stack.pop()
        if temp == self.min[0]:
            self.min.remove(temp)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[0]