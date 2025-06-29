class Solution {
public:
    int reverse(int x) {
    long long val = x;
    bool isNegative = val < 0;
    if (isNegative) val = -val;

    string s = to_string(val);
    int size = s.size();
    for (int i = 0; i < size / 2; i++) {
            swap(s[i], s[size - 1 - i]);
    }

    long long reversed = stoll(s);
    if (reversed > INT_MAX) return 0;

    return isNegative ? -reversed : reversed;
    }
};
