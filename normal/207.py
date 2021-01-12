from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses

# 自己写的拓扑排序
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = []
        ans = defaultdict(int)
        count = 0
        sontof = defaultdict(list)
        ftoson = defaultdict(list)

        for i, j in prerequisites:
            ftoson[j].append(i)
            sontof[i].append(j)
        
        for k, v in sontof.items():
            ans[k] = len(v)
   
        for i in range(numCourses):
            if ans[i] == 0:
                todo.append(i)
                ans.pop(i)

        while todo:
            needtopop = []
            count += 1
            t = todo.pop()
            for k in ftoson[t]:
                ans[k] -= 1
            for k, v in ans.items():
                if v == 0:
                    needtopop.append(k)
                    todo.append(k)
            for tmp in needtopop:
                ans.pop(tmp)

        return count == numCourses
