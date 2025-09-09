class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0, 1]        
        shareable, result = 0, 0
        MOD = 10**9 + 7
        for i in range(2, n + 1):
            if i - delay >= 1:
                shareable = (shareable + dp[i - delay]) % MOD
            if i - forget >= 1:
                shareable = (shareable - dp[i - forget]) % MOD
            dp.append(shareable)

        for i in range(n - forget + 1, n + 1):
            result = (result + dp[i]) % MOD

        return result
