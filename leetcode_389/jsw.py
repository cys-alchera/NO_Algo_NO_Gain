class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for tt in t:
            if tt not in s:
                return tt
            else:
                s = s.replace(tt,'', 1)