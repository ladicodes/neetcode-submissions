class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        if len(s) != len(t):
            return False
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True