class Solution {
public:
    int search(vector<int>& nums, int target) {
        int size = nums.size();
        int rotation;
        for (int i = 0; i < size; i++) {
            int j;
            for (j = 0; j < size - 1; j++) {
                if (nums[(j + i + 1) % size] < nums[(j + i) % size]) break;
            }
            if (j == size - 1) {
                rotation = i;
                break;
            }

        }
        
        int left = 0, right = size - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int realMid = (mid + rotation) % size;

            if (nums[realMid] == target) return realMid;
            else if (nums[realMid] < target) left = mid + 1;
            else right = mid - 1;
        }

        return -1;

    }
};search-in-rotated-sorted-array
