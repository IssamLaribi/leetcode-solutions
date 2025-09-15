class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        words_num = len(words)
        for word in words:
            for c in brokenLetters:
                if c in word:
                    words_num -= 1
                    break

        return words_num
