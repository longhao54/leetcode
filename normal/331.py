class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        left, right = 0, 0
        preorder = preorder.split(",")
        if ["#"] == preorder:
            return True
        c = 0
        for i in preorder:
            if right < 0 or left < 0:
                return False
            if i != "#":
                if left == 0 and right == 0:
                    if c != 0:
                        return False
                    left += 1
                    right += 1
                    c += 1
                elif left != 0:
                    left += 1
                else:
                    right += 1
            else:
                if left != 0:
                    left -= 1
                else:
                    right -= 1
        return left == 0 and right == 0
    
# 最快答案
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        edges = 1
        for item in preorder:
            edges -= 1
            if edges < 0: return False
            if item != "#":
                edges += 2
        return edges == 0
