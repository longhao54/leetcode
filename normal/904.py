class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        s = {}
        left, right = 0, 0
        ans = 0
        while right < len(tree):
            if tree[right] not in s:
                s[tree[right]] = 1
            else:
                s[tree[right]] += 1
            right += 1
            
            while len(s) > 2:
                t = tree[left] 
                s[t] -= 1
                if s[t] == 0:
                    s.pop(t)
                left += 1
            ans = max(ans, right-left)    
        return ans
