def generate_hashtag(s):
    
    if s == '':
            return False #meow
    
    s2 = s.strip(" ")
    s_list = s2.split()
    s2_list = []
    
    for string_member in s_list:
        
        if len(string_member) > 140:
            return False
        
        else:
            
            Cm = string_member.capitalize()
            s2_list.append(Cm)
    
    if len(f'#{"".join(s2_list)}') > 140:
        return False
    else:
        return f'#{"".join(s2_list)}'