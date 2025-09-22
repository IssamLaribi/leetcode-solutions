class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        max_freq = 0
        ans = 0
        
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
            freq = frequencies[n]
            
            if freq > max_freq:
                max_freq = freq
                ans = freq
            elif freq == max_freq:
                ans += freq
        
        return ans
