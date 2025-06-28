class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> PascalRows;
        PascalRows.push_back({1});
        if (numRows == 1) return PascalRows;
        for (int i = 2; i <= numRows; i++) {
            vector<int> PascalRow(i);
            PascalRow[0] = 1;
            PascalRow[i - 1] = 1; 
            for (int j = 1; j <= i - 2; j++) {
                PascalRow[j] = PascalRows[i - 2][j - 1] + PascalRows[i - 2][j];
            }
            PascalRows.push_back(PascalRow);
        }
        return PascalRows;
    }
};
