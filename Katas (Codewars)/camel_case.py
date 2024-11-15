def camel_case(s):
    
    new_cl = []
    cl = s.split()
    print(len(cl))
    
    
    if len(cl) == 2:
        for x in cl:
            y = x.capitalize()
            print(y)
            new_cl.append(y)
        return "".join(new_cl)
            
    elif len(cl) >= 3:
        for x in cl:
            y = x.capitalize()
            print(y)
            new_cl.append(y)
        return "".join(new_cl)
    else:
        return s
    
    pass