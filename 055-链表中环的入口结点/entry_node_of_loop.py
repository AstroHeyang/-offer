def entry_node_of_loop(pHead):
	# write code here
	if not pHead or not pHead.next:
	    return None
	
	fast, slow = pHead, pHead
	has_circle = False
	while fast and fast.next:
	    fast = fast.next.next
	    slow = slow.next
	    if fast.val == slow.val:
	        has_circle = True
	        break
	if not has_circle:
	    return None
	while pHead.val != slow.val:
	    pHead = pHead.next
	    slow = slow.next
	return pHead
