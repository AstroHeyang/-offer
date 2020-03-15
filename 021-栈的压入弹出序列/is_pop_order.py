def is_pop_order(pushV, popV):
    if not pushV or not popV:
        return
    tmp_stack = []
    while popV:
        if pushV and pushV[0] == popV[0]:
            pushV.pop(0)
            popV.pop(0)
        elif tmp_stack and tmp_stack[-1] == popV[0]:
            tmp_stack.pop()
            popV.pop(0)
        elif pushV:
            tmp_stack.append(pushV.pop(0))
        else:
            return False
    return not tmp_stack
