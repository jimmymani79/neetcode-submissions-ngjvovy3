class Solution:
    def apply(self, op, op1, op2):
        match op:
            case "+":
                return op2 + op1
            case "-":
                return op2 - op1
            case "*":
                return op2 * op1
            case "/":
                return int(op2 / op1)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                stack.append(self.apply(t, stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
            print(stack)
        return stack[-1]


        