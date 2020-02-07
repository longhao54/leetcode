class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.d

    def add(self, key: int) -> None:
        self.d[key] = True

    def remove(self, key: int) -> None:
        if key in self.d:
            self.d.pop(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.d.get(key, False)
