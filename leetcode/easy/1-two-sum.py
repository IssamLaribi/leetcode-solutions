class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        # use index, value for 
        for i, num in  enumerate(nums):
            complement = target - nums[i]
            if complement in mp: 
                return [mp[complement],i]

            mp[num] = i 

        return []
         
