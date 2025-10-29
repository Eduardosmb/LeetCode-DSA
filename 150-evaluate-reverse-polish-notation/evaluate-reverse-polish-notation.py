class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for c in tokens:
            if c in operators:
                n1 = int(stack[-2])
                n2 = int(stack[-1])
                stack.pop()
                stack.pop()

                if c == '+':
                    stack.append(n1+n2)
                elif c == '-':
                    stack.append(n1-n2)
                elif c == '*':
                    stack.append(n1*n2)
                else:
                    stack.append(n1/n2)
            else:
                stack.append(c)
        
        return int(stack[0])


                