class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        digits[size - 1]++;
        while (size - 1 > 0) {
            if (digits[size - 1] >= 10) {
                digits[size - 2]++;
                digits[size - 1] -= 10;
                size--;
            } else if (digits[size - 1] < 10) return digits;
        }
        if (digits[0] >= 10) {
            digits[0] -= 10;
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
