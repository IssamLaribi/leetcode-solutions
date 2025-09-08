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

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  
                top_element = stack.pop() if stack else ''
                if mapping[char] != top_element:
                    return False
            else:  
                stack.append(char)

        return not stack
