class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.cells[(row, col)] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        if (row, col) in self.cells:
            del self.cells[(row, col)]

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split('+')

        def get_val(token: str) -> int:
            if token[0].isalpha():
                col = ord(token[0]) - ord('A')
                row = int(token[1:]) - 1
                return self.cells.get((row, col), 0)
            return int(token)

        return get_val(left) + get_val(right)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
