class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            for c in set(s):
                if s.count(c) != t.count(c):
                    return False
                    
            return True

        allAnagrams = []
        i = 0

        while i < len(strs):
            anagrams = [strs[i]]
            j = i + 1

            while j < len(strs):
                if isAnagram(strs[i], strs[j]):
                    anagrams.append(strs[j])
                    del strs[j]
                else:
                    j += 1
                
            allAnagrams.append(anagrams)
            i += 1

        return allAnagrams



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
      
        for s in strs:
            ans.setdefault(tuple(sorted(s)), []).append(s)
          
        return list(ans.values())
