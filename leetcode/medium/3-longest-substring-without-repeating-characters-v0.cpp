class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        if (size == 0) 
            return 0;

        int maxlength = 0;

        set<char> chars;
        int left = 0;
        for (int right = 0; right < size; right++) {
            while (chars.count(s[right])) {
                chars.erase(s[left]);
                left++;
            }
            chars.insert(s[right]);
            maxlength = max(maxlength, right - left + 1);
        }
        return maxlength;
    }
};
