class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x = 0
        y = 0
        for i in instructions:
            if i == 'L':
                direction -= 1
            elif i == 'R':
                direction += 1
            else:
                direction %= 4
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                else:
                    x -= 1
        return direction % 4 != 0 or (x == 0 and y == 0)
