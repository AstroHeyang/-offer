class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 非递归
def reverseList(head):
    if not head or not head.next:
        return head
    preNode = None
    curNode = head
    while curNode and curNode.next:
        preNode, curNode, curNode.next = curNode, curNode.next, preNode
    return head


# 递归
def reverseList(head):
    if not head or not head.next:
        return head
    preNode = reverseList(head.next)
    head.next.next = head
    head.next = None
    return preNode
