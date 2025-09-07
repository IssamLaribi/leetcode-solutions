class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Base case: both string and pattern empty
        if not s and not p:
            return True
        
        # Base case: pattern empty, string not empty
        if not p and s:
            return False
        
        # Base case: string empty, pattern not empty
        if not s and p:
            # pattern can only match empty if it consists of x* pairs
            if len(p) % 2 == 1:
                return False
            for i in range(1, len(p), 2):
                if p[i] != '*':
                    return False
            return True

        # Check if first characters match
        first_match = (s[0] == p[0] or p[0] == '.')

        # Handle '*' in the pattern
        if len(p) >= 2 and p[1] == '*':
            # Option 1: skip '*' and previous character
            # Option 2: if first character matches, consume one char from s
            return (self.isMatch(s, p[2:]) or
                    (first_match and self.isMatch(s[1:], p)))
        else:
            # No '*', continue character by character
            return first_match and self.isMatch(s[1:], p[1:])
