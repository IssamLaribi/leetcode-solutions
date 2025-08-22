public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1 || s.Length <= numRows) return s;

        StringBuilder[] rows = new StringBuilder[Math.Min(numRows, s.Length)];
        for (int i = 0; i < rows.Length; i++) {
            rows[i] = new StringBuilder();
        }

        int currentRow = 0;
        bool goingDown = false;

        foreach (char c in s) {
            rows[currentRow].Append(c);

            // Change direction when we reach top or bottom
            if (currentRow == 0 || currentRow == numRows - 1)
                goingDown = !goingDown;

            currentRow += goingDown ? 1 : -1;
        }

        StringBuilder result = new StringBuilder();
        foreach (var row in rows) {
            result.Append(row);
        }

        return result.ToString();
    }
}
