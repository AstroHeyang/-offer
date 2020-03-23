class RandomListNode:
    def __init__(self):
        self.val = val
        self.next = None
        self.random = None


def clone(head):
    if not head:
        return None

    # 复制链表，但不包括随机指针
    current_node = head
    while current_node:
        clone_node = RandomListNode(current_node.val)
        next_node = current_node.next
        current_node.next = clone_node
        clone_node.next = next_node
        current_node = next_node

    # 复制随机指针
    current_node = head
    while current_node:
        random_node = current_node.random if current_node.random else None
        current_node.next.random = random_node.next if random_node else None
        current_node = current_node.next.next

    # 拆分出复制链表
    clone_head = current_node.next
    while current_node:
        clone_node = current_node.next
        current_node.next = clone_node.next
        clone_node.next = clone_node.next.next if clone_node.next else None
        current_node = current_node.next

    return clone_head

