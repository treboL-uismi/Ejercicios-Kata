def disemvowel(string_):
    
    for x in 'aeiouAEIOU':
        string_ = string_.replace(x, '')
    
    return string_