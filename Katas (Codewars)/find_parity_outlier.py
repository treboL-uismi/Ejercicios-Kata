def find_outlier(integers) -> int:
    
    odd_list = [] 
    even_list = []
        
    for e in integers:
        if e % 2 == 0:
            odd_list.append(e)
        else:
            even_list.append(e)
        
    if len(odd_list) > len(even_list):
        return even_list[0]
    else:
        return odd_list[0]