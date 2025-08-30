class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check each row
        for (int i = 0; i < 9; i++) {
            bool seen[9] = {false};
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    if (seen[num]) return false;
                    seen[num] = true;
                }
            }
        }

        // Check each column
        for (int j = 0; j < 9; j++) {
            bool seen[9] = {false};
            for (int i = 0; i < 9; i++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    if (seen[num]) return false;
                    seen[num] = true;
                }
            }
        }

        // Check each 3x3 sub-box
        for (int boxRow = 0; boxRow < 3; boxRow++) {
            for (int boxCol = 0; boxCol < 3; boxCol++) {
                bool seen[9] = {false};
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        int r = boxRow * 3 + i;
                        int c = boxCol * 3 + j;
                        if (board[r][c] != '.') {
                            int num = board[r][c] - '1';
                            if (seen[num]) return false;
                            seen[num] = true;
                        }
                    }
                }
            }
        }

        return true;
    }
};

