class Solution:
    def removeDuplicates(self, S: str) -> str:
        start = 0
        lenth = S.__len__() - 1
        S = list(S)
        last = 0
        while start < lenth:
            if S[start] == S[start+1]:
                S.pop(start)
                S.pop(start)
                lenth -= 2
                start = last
            else:
                last = start-1 if start != 0 else 0
                start += 1
        return "".join(S)
        

    def fast(self, S):
        r = []
		for c in s:
			if r and c == r[-1]:
				r.pop()
				continue
			r.append(c)
		return ''.join(r)
