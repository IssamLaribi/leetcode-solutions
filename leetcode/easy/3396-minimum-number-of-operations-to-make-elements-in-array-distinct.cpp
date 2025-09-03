class Solution {
private: 
    bool isDistinct(vector<int>& nums, int start) {
        for (int i = start; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j]) return false;
            }
        }
        return true;
    }

    int helper(vector<int>& nums, int start) {
        if (isDistinct(nums, start)) return 0;

        int newStart = min(start + 3, (int)nums.size());
        return 1 + helper(nums, newStart);
    }

public:
    int minimumOperations(vector<int>& nums) {
        return helper(nums, 0);
    }
};

