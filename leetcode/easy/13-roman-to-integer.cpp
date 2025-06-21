class Solution {
public:
    int romanToInt(string s) {
        int intValue = 0;
        int size = s.size();
        for (int i = 0; i < size; i++) {
            if (s[i] == 'I') {
                if (s[i + 1] == 'V') {
                    intValue += 4;
                    i++;
                } else if (s[i + 1] == 'X') {
                    intValue += 9;
                    i++;
                } else {
                    intValue += 1;
                }
            } else if (s[i] == 'X') {
                if (s[i + 1] == 'L') {
                    intValue += 40;
                    i++;
                } else if (s[i + 1] == 'C') {
                    intValue += 90;
                    i++;
                } else {
                    intValue += 10;
                }
            } else if (s[i] == 'C') {
                if (s[i + 1] == 'D') {
                    intValue += 400;
                    i++;
                } else if (s[i + 1] == 'M') {
                    intValue += 900;
                    i++;
                } else {
                    intValue += 100;
                }
            } else if (s[i] == 'V')
                intValue += 5;
            else if (s[i] == 'L')
                intValue += 50;
            else if (s[i] == 'D')
                intValue += 500;
            else if (s[i] == 'M')
                intValue += 1000;
        }
        return intValue;
    }
};
