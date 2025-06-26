class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = s.size();
        int lenght = 0;
        while (size - 1 >= 0) {
            if (s[size - 1] == ' ') {
                if (lenght != 0) return lenght;
                else size--;
            }
            else {
                lenght++;
                size--;
            }
        } 
        return lenght;
    }
};
