class Solution {
public:
    bool check(vector<int>& nums) {
        int size = nums.size();
        if (size == 1) return true;
        for (int x = 0; x < size; x++) {
            for (int i = 0; i < size - 1; i++) {
                if (nums[(i + x + 1) % size] < nums[(i + x) % size]) break;
                if (i == size - 2 && nums[(i + x + 1) % size] >= nums[(i + x) % size]) return true;
            }
        }
        return false;
    }
};
