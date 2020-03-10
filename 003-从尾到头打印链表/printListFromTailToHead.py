class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 递归
def printListFromTailToHead_recursion(listNode):
    if not listNode:
        return []
    return printListFromTailToHead(listNode.next) + [listNode.val]


# 借用辅助栈
def printListFromTailToHead_stack(listNode):
    if not listNode:
        return []
    stack = []
    tmpNode = listNode
    while not tmpNode:
        stack.append(tmpNode.val)
        tmpNode = tmpNode.next
    res = []
    while not stack:
        res.append(stack.pop())
    return res

