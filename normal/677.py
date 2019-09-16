class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ans = {}

    def insert(self, key: str, val: int) -> None:
        self.ans[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for key in self.ans:
            if key.startswith(prefix):
                ans += self.ans[key]
        return ans


