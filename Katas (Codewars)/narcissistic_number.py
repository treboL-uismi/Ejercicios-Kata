def narcissistic(value):
    
    x = list(str(value))
    y = []
    
    for i in x:
        raisepow = pow(int(i), len(x))
        y.append(raisepow)
        
    nar = sum(y)
    
    if nar == value:
        return True
    else:
        return False