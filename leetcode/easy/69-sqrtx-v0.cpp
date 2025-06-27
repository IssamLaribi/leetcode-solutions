class Solution {
public:
    int mySqrt(int x) {
        int i = 1;
        while (i < 46341) {
            if (x == i * i) return i;
            if (x < i * i) return i - 1;
            i++;
        }
        return i - 1;
    }
};
