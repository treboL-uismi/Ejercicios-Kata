def digital_root(n):
    b = 0
    a = list(str(n))
    
    for d in a:
        b += int(d)
    
    if len(str(b)) > 1:
        return digital_root(b)
    else:
        return b