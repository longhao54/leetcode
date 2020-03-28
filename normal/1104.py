class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        while label:
            label = 3 * 2**(len(bin(label))-3) - 1 - label
            label //= 2
            ans.insert(0, label)
        return ans[1:]

