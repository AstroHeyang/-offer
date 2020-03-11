
stack1 = []
stack2 = []


def push(val):
    stack1.append(val)


def pop():
    if stack2:
        return stack2.pop()
    elif stack1:
        while stack1:
            stack2.append(stack1.pop())
        return stack2.pop()
    else:
        return
