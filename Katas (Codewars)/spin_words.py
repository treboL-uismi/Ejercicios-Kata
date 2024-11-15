def spin_words(sentence):
    return " ".join([l[::-1] if len(l) >= 5 else l for l in sentence.split()])