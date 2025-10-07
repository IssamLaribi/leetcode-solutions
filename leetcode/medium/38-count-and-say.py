class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            new_s = ""
            count = 1
            for i in range(1, len(s) + 1):
                if i < len(s) and s[i] == s[i - 1]:
                    count += 1
                else:
                    new_s += str(count) + s[i - 1]
                    count = 1
            s = new_s
        return s
