class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 递归
def merge(pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1

    if pHead1.val <= pHead2.val:
        res = pHead1
        res.next = merge(pHead1.next, pHead2)
    else:
        res = pHead2
        res.next = merge(pHead1, pHead2.next)
    return res


# 非递归
def merge(pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1

    res = mergeHead = ListNode(0)
    while pHead1 and pHead2:
        if pHead1.val >= pHead2.val:
            mergeHead.next = pHead1
            pHead1 = pHead1.next
        else:
            mergeHead.next = pHead2
            pHead2 = pHead2.next
        mergeHead = mergeHead.next

    mergeHead.next = pHead1 if pHead1 else pHead2
    return res.next


