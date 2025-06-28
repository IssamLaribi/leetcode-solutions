class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> PascalRows;
        PascalRows.push_back({1});
        if (rowIndex == 0) return PascalRows[0];
        for (int i = 1; i <= rowIndex; i++) {
            vector<int> PascalRow(i + 1);
            PascalRow[0] = 1;
            PascalRow[i] = 1; 
            for (int j = 1; j <= i - 1; j++) {
                PascalRow[j] = PascalRows[i - 1][j - 1] + PascalRows[i - 1][j];
            }
            PascalRows.push_back(PascalRow);
        }
        return PascalRows[rowIndex];
    }
};
