class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.size() - 1;
        int n = b.size() - 1;
        string result = "";
        bool carry = false;

        while (m >= 0 || n >= 0 || carry) {
            int sum = carry ? 1 : 0;
            if (m >= 0) sum += a[m--] - '0';
            if (n >= 0) sum += b[n--] - '0';
            result.insert(result.begin(), sum % 2 + '0');
            carry = sum > 1;
        }

        return result;
    }
};
