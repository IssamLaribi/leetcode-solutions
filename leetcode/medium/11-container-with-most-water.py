class Solution:
    def maxArea(self, height: List[int]) -> int:
        left ,right = 0, len(height)-1
        h = min(height[left], height[right])
        max_area = h * (right-left)
        while left != right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            h = min(height[left], height[right])
            max_area = max(max_area, h*(right-left))
        return max_area
