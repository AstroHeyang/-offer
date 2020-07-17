def get_ugly_number(index):
    if index <= 0:
        print('Error! Index should be larger than 0!')
        return 0
    ugly_number_list = [1]
    index_2, index_3, index_5 = 0, 0, 0
    i = 1
    while i < index:
        next_ugly_number = min( \
            2*ugly_number_list[index_2], \
            3*ugly_number_list[index_3], \
            5*ugly_number_list[index_5])
            
        ugly_number_list.append(next_ugly_number)
        i += 1
        if 2*ugly_number_list[index_2] == next_ugly_number:
            index_2 += 1
        if 3*ugly_number_list[index_3] == next_ugly_number:
            index_3 += 1
        if 5*ugly_number_list[index_5] == next_ugly_number:
            index_5 += 1
            
    return ugly_number_list[index-1]
    
