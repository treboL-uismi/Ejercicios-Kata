def DNA_strand(dna):
    alt = {"A": "T", "G": "C", "T": "A", "C": "G"}
    return "".join([alt[x] for x in dna])