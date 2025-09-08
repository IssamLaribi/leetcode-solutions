class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        size = len(s)
        if size % 2 == 1:
            return False

        for i in range(size):
            if s[i] in {'(', '[', '{'}:
                stack.append(s[i])

            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else: 
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else: 
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else: 
                    return False
        
        return not stack
