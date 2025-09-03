class Solution {
private: 
    int sum(vector<int> nums) {
        int sum = 0;
        for (int n : nums) sum += n;
        return sum;
    }

public:
    bool canPartition(vector<int>& nums) {
        int target = sum(nums);
        // If total sum is odd, cannot partition into two equal subsets
        if (target % 2 == 1) return false;
        
        // we just need to see if there's a subset with this sum
        target /= 2;
        
        bool possible[target + 1];
        possible[0] = true; // base case: sum 0 is always possible
        for (int i = 1; i < target + 1; i++) possible[i] = false;

        for (int n : nums) {
            for (int i = target; i >= n; i--) {
                if (possible[i - n]) {
                    possible[i] = true;
                }
            }
        }
        return possible[target];
    }
};
