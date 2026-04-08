class Solution:
    def apply(self, op, op1, op2):
        match op:
            case "+":
                return int(op2) + int(op1)
            case "-":
                return int(op2) - int(op1)
            case "*":
                return int(op2) * int(op1)
            case "/":
                return int(int(op2) / int(op1))
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                stack.append(self.apply(t, stack.pop(), stack.pop()))
            else:
                stack.append(t)
            print(stack)
        return int(stack[-1])


        