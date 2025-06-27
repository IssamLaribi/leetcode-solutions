class Solution {
public:
    long long int binarySearch(int n) {
        long long int begin = 0, end = n;
        int sqrt = -1;
        while (begin <= end) {
            long long int mid = begin + (end - begin) / 2;
            if (mid * mid == n) return mid;
            else if (mid * mid > n) end = mid - 1;
            else begin = mid + 1;
        }
        return begin - 1;
    }
    int mySqrt(int x) {
        return binarySearch(x);
    }
};
