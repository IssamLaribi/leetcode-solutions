class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        if (size == 0) return 0;

        vector<int> v;

        for (int i = 0; i < size; i++) {
            if (nums[i] != val) v.push_back(nums[i]);
        }

        size = v.size();
        for (int i = 0; i < size; i++) {
            nums[i] = v[i];
        }
        return size;
    }
};
