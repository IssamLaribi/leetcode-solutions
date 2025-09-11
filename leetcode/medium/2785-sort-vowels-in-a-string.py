class Solution:
    def sortVowels(self, s: str) -> str:
        t = ""
        vowels = []
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                vowels.append(c)

        vowels.sort()
        v = 0
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                t += vowels[v]
                v += 1
            else:
                t += c
        return t
