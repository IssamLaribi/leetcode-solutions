class Solution:
    def maxFreqSum(self, s: str) -> int:
        keys = set(s) 
        consts = dict.fromkeys(keys, 0)
        vowels = dict.fromkeys(keys, 0)
        v = {'a', 'e', 'i', 'o', 'u'}

        for c in s:
            if c in v:
                vowels[c] += 1
            else: 
                consts[c] += 1

        consts = list(consts.values())
        vowels = list(vowels.values())
        
        return max(vowels) + max(consts)
