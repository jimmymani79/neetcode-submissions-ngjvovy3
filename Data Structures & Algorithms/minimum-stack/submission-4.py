class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []
    
    def top(self)-> int:
        if not self._stack: return None
        return self._stack[-1]
    
    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(val, self._min_stack[-1]))
    
    def pop(self) -> None:
        if self._min_stack and self._stack:
            self._min_stack.pop()
            self._stack.pop()
    
    def getMin(self) -> int:
        if not self._min_stack: return None
        else:
            return self._min_stack[-1]
        
