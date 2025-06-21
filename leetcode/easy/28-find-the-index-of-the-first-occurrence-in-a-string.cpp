class Solution {
public:
    int strStr(string haystack, string needle) {
        int haystackSize = haystack.size();
        int needleSize = needle.size();
        for (int i = 0; i < haystackSize - needleSize + 1; i++) {
            for (int j = i; j < i + needleSize; j++) {
                if (haystack[j] != needle[j - i]) break;
                else if (j == i + needleSize - 1) return i;
            }
        }
        return -1;
    }
};
