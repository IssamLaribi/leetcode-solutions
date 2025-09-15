class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        start, end = 1, max_speed
        ans = 1
        while start <= end:
            mid = start + (end - start) // 2
            hours_spent = 0
            for pile in piles:
                hours_spent += ceil(pile / mid)

            if hours_spent == h or hours_spent < h:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans
        
