def delete_duplicate(pHead):
	# write code here
	if not pHead:
	    return
	dummy = ListNode(-1)
	dummy.next = pHead
	pre, cur = dummy, pHead
	while cur and cur.next:
	    if cur.val != cur.next.val:
	        pre = pre.next
	        cur = cur.next
	    else:
	        cur_val = cur.val
	        while cur and cur.val == cur_val:
	            cur = cur.next
	        pre.next = cur
	return dummy.next
