class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1=list(s).sort()
        # t1=list(t).sort()
        # # s1.sort()
        # # t1.sort()
        return sorted(s)==sorted(t)
        