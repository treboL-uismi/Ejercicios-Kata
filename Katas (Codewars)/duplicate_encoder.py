def duplicate_encode(word):
    word = word.lower()
    word_toRet = ''
    for char in word:
        if word.count(char)  > 1:
            word_toRet += ')'
        else:
            word_toRet += '('
    return word_toRet