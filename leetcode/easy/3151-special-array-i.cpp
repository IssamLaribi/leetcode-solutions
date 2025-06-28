class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        vector<vector<int>> allPairs;
        int size = nums.size();
        if (size == 1) return true;
        for (int i = 0; i < size - 1; i++){
            if ((nums[i] - nums[i + 1]) % 2 == 0) return false;
        }
        return true;
    }
};
