class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        index = 0
        l = len(s)
        def split(lines):
            if not lines:
                return 0
            c = 1
            count = 1
            while c != 0 and count < len(lines):
                if lines[count] == ")":
                    c -= 1
                elif lines[count] == "(":
                    c += 1
                count += 1
            return count
             
        def check(lines):
            if lines.startswith("()"):
                return None
            if lines:
                c = 0
                while c < len(lines) and lines[c] not in "()":
                    c += 1
                root = TreeNode(lines[0:c])
                ls = split(lines[c:])
                root.left = check(lines[c+1:ls+c-1])
                if lines[ls+2:-1]:
                    root.right = check(lines[ls+c+1:-1])
                return root
        return check(s)
