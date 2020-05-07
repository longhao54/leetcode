class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head):
        if head == None:
            return None
        if head in self.visitedHash:
            return self.visitedHash[head]
        node = Node(head.val, None, None)
        self.visitedHash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node



class Solution(object):
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node != None:

            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

