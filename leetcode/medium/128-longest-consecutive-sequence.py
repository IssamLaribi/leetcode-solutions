class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums = set(nums)

        for n in nums:
            current_streak = 1
            if n - 1 not in nums:
                while n + current_streak in nums:
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
