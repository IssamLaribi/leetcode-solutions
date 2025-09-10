class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCountTable = {}  
        tCountTable = {}  

        for c in s:
            sCountTable[c] = sCountTable.get(c, 0) + 1

        for c in t:
            tCountTable[c] = tCountTable.get(c, 0) + 1

        return sCountTable == tCountTable

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False
                
        return True
