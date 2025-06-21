class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) return 0;

        vector<int> v;
        for (int i = 0; i < size - 1; i++) {
            if (nums[i] != nums[i + 1]) v.push_back(nums[i]);
        }
        // Add last element
        v.push_back(nums[size - 1]);
        size = v.size();
        // Copy the elements of v to nums
        for (int i = 0; i < size; i++) {
            nums[i] = v[i];
        }
        return size;
    }
    };
