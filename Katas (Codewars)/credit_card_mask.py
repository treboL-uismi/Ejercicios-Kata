def maskify(cc):
    
    masked = "#"*(len(cc) - 4)
    unmasked = cc[-4:]
    
    if len(cc) < 4:
        return cc
    return masked+unmasked