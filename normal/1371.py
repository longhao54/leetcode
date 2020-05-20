class Solution:
	def findTheLongestSubstring(self,s:str)->int:
		l,ans,state=[0]+[-1]*31,0,0
		for i in range(len(s)):
			if s[i] in 'aeiou':state^=1<<'aeiou'.find(s[i])
			if ~l[state]:ans=max(ans,i+1-l[state])
			else:l[state]=i+1
		return ans
