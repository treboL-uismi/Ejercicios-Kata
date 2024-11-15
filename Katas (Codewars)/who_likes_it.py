def likes(names):
    
    if len(names) == 0:
        name = 'no one likes this'
    elif len(names) == 1:
        name = f'{names[0]} likes this'
    elif len(names) == 2:
        name = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        name = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        name = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
        
    return name