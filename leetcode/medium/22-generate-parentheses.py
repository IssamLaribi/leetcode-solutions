class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combination = ""

        def helper(combination, open, close):
            if open == 0 and close == 0:
                result.append(combination)
                combination = ""

            if open > 0:
                helper(combination + '(', open - 1, close)
            
            if close > open: 
                helper(combination + ')', open, close - 1)

        helper(combination, n, n)
        return result
