def find_first_common_node(pHead1, pHead2):
    p1,p2 = pHead1,pHead2
    while p1!=p2:
		p1 = p1.next if p1 else pHead2
        p2 = p2.next if p2 else pHead1
    return p1
            
