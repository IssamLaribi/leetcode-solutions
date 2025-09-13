class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    o2 = stack.pop()
                    stack.append(stack.pop() - o2)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    o2 = stack.pop()
                    stack.append(int(stack.pop() / o2))
                case _:
                    stack.append(int(token))

        return stack.pop()
