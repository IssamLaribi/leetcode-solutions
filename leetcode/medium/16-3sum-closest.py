class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] 

        nums.sort()
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:  
                    return target
            

        return closest_sum
