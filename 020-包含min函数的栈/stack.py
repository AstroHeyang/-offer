class Stack:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, num):
        self.stack.append(num)
        if not self.stack_min:
            self.stack_min.append(num)
        else:
            if num >= self.stack_min[-1]:
                self.stack_min.append(self.stack_min[-1])
            else:
                self.stack_min.append(num)

    def pop(self):
        if not self.stack:
            return None
        else:
            self.stack_min.pop()
            return self.stack.pop()

    def min(self):
        if not self.stack_min:
            return None
        else:
            return self.stack_min[-1]

    def top(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]

