class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        t = set()
        for i in emails:
            t1, t2 = i.split("@")
            t1 = t1.split("+")[0].replace(".","")
            t.add(t1+"@"+t2)
        return len(t)
