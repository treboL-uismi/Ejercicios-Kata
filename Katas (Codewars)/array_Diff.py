def array_diff(a, b):
    
    c = []
    
    for i in a:
        if i not in b:
            
            c.append(i)
        
    return c