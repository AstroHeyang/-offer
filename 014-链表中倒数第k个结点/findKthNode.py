class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def findKthNode(head, k: int):
    if not head or k < 1:
        return
    fast, slow = head, head
    while k > 1:
        if not fast.next:
            return
        fast = fast.next
        k -= 1
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    return slow
