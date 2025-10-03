from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_valid(r, c, ch):
            # check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            # check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            # check 3x3 sub-box
            box_row, box_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1, 10)):
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        backtrack()
