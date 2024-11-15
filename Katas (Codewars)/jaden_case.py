def to_jaden_case(string) -> str:
    Jc = []
    divi = string.split() # divi = ['How', 'can' ...]
    
    for i in divi: # 'How'
        x = i.capitalize() 
        Jc.append(x)
        
    jaden_case = (' '.join(Jc))
        
    return jaden_case