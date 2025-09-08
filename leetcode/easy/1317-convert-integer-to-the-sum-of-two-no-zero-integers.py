class Solution:
    def has_zero(self, n: int) -> bool:
        return "0" in str(n)

    def getNoZeroIntegers(self, n: int) -> List[int]:
        i, j = 1, n - 1

        while i <= j:
            if not self.has_zero(i) and not self.has_zero(j):
                return [i, j]
            else: 
                i += 1
                j -= 1
