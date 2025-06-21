class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int xdigits = digits(x);
        if (xdigits == 1) return true;
        int temp = x;
        int tempdigits = xdigits;
        while (tempdigits > 1) {
            int rdigit = temp % 10;
            int ldigit = temp / pow(10, tempdigits - 1);
            if (rdigit != ldigit) return false;
            temp -= ldigit * pow(10, tempdigits - 1);
            temp /= 10;
            tempdigits -= 2;
        }       
        return true;
    }
    int digits(int x) {
        int count = 0;
        if (x == 0) return 1;
        while (x > 0) {
            x /= 10;
            count++;
        }
        return count;
    }
};
