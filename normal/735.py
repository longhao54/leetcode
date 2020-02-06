class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = []
        right = []
        for i in asteroids:
            if i > 0:
                right.append(i)
            else:
                while right:
                    t = right.pop()
                    if t > abs(i):
                        i = 0
                        right.append(t)
                        break
                    elif t == abs(i):
                        i = 0
                        break
            if i < 0:
                left.append(i)
        return left + right
