class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        if (size == 0) 
            return 0;

        int maxlength = 0;
        int hash[256];
        for (int i = 0; i < 256; i++) hash[i] = -1;
        int left = 0, right = 0;
        while (right < size) {
            if (hash[s[right]] == -1 || hash[s[right]] < left) {
                hash[s[right]] = right;
                maxlength = max(maxlength, right - left + 1);
                right++;
            } else {
                left = hash[s[right]] + 1;
                hash[s[right]] = right;
                right++;
            }
        }

        return maxlength;
    }
};
