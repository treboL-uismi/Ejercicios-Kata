def snail(snail_map):
    
    if snail_map == [[]]: return []

    ret = []
    
    while len(snail_map) > 0:
        
        ret += snail_map[0] #pilla la primera fila y la pasa al nuevo array
        del snail_map[0] #borra la fila del array anterior y queda [[4,5,6], 
                                                                  # [7,8,9]]
        
        if len(snail_map) <= 0: break #una forma para prevenir errores
        
        for row in snail_map:
            ret += [row[-1]] # pilla el 6 y el 9, ya que son los últimos miembros de cada fila
            del row[-1]
            
            # [[4,5],  <-- así quedara al final
            #  [7,8]]
            
        if len(snail_map) <= 0: break
        
        ret += snail_map[-1][::-1] #pilla el 8 y el 7
        
        del snail_map[-1]
        
        if len(snail_map) <= 0: break
        
        for row in reversed(snail_map): #y ahora a por el 4 y el 5
            ret += [row[0]]
            del row[0]
            
    return ret