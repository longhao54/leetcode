class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        nums = []
        dic = {}
        if not root:
            return None
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                nums.append(t.val)
                dp.append(t.left)
                dp.append(t.right)
                dic[t.val] = Node(t.val)
        nums.sort()
        lenth = len(nums)
        if lenth == 1:
            dic[nums[0]].right = dic[nums[0]]
            dic[nums[0]].left = dic[nums[0]]
            return dic[nums[0]]
        for i in range(lenth):
            if i == 0:
                dic[nums[i]].right = dic[nums[i+1]]
                dic[nums[i]].left = dic[nums[lenth-1]]
            elif i == lenth -1:
                dic[nums[i]].right = dic[nums[0]]
                dic[nums[i]].left = dic[nums[i-1]]
            else:
                dic[nums[i]].right = dic[nums[i+1]]
                dic[nums[i]].left = dic[nums[i-1]]
        return dic[nums[0]]


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        self.prev = None
        self.dfs(root)
        while root.left:
            root = root.left
        self.prev.right = root
        root.left = self.prev
        return root
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.prev:
            self.prev.right = root
            root.left = self.prev
        self.prev = root
        self.dfs(root.right)
