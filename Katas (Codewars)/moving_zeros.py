def move_zeros(lst):
    
    copy_lst = lst
    
    new_lst = []
    
    for number in lst:
        if number == 0:
            new_lst.append(number)
        else:
            pass
        
    for n in copy_lst:
        for zero in new_lst:
            if n == zero:
                copy_lst.pop(copy_lst.index(n))
        
        
    lst = lst + new_lst
    
    return lst