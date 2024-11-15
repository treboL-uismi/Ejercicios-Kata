def alphabet_position(text):
    
    listA = list("abcdefghijklmnopqrstuvwxyz")
    
    return " ".join([str(listA.index(letter) + 1) for letter in text.lower() if letter in listA])