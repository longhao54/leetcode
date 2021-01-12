class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        todo = []
        final = []
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
            final.append(t)
            for k in ftoson[t]:
                ans[k] -= 1
            for k, v in ans.items():
                if v == 0:
                    needtopop.append(k)
                    todo.append(k)
            for tmp in needtopop:
                ans.pop(tmp)

        return final if len(final) == numCourses else []
