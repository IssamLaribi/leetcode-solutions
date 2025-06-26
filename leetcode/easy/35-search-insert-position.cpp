class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int begin = 0;
        int end = nums.size() - 1;
        while (begin <= end) {
            int mid = begin + (end - begin) / 2;
            if (target > nums[mid]) {
                begin = mid + 1;
            } else if (target < nums[mid]) {
                end = mid - 1;
            } else {
                return mid;
            }
        }
        return begin;
    }
};
