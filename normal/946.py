class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        t1 = []
        for i in pushed:
            t1.append(i)
            while t1:
                if t1[-1] == popped[0]:
                    t1.pop()
                    popped.pop(0)
                else:
                    break
        return True if not t1 else False 
