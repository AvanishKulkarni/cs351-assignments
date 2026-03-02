from collections import Counter
'''
CS 351 Assignment 3
Allen Cabrera
Avanish Kulkarni
Youssef Masoud
'''
def decode(ciphertext, mapping):
    # decode the ciphertext using the mapping
    decoded = ""
    for c in ciphertext:
        if c.isalpha():
            decoded += mapping[c.upper()]
        else:
            decoded += c

    return decoded

if __name__ == "__main__":

    # clean user input to alphabetic only
    ciphertext = input("Enter ciphertext:\n")
    clean = "".join(c.upper() for c in ciphertext if c.isalpha())

    # get letters ordered by freq
    count = Counter(clean).most_common()
    freq, _ = zip(*count)

    # map frequencies to known English letter frequencies
    # source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    eng_freq = ['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

    # create mapping from ciphertext letters to English letters
    mapping = {c.upper(): e.upper() for c, e in zip(freq, eng_freq)}
    
    print(decode(ciphertext, mapping))

    # ask user to refine mapping if needed
    while True:
        r_c = input("What character do you want to replace from the cipher? (type 0 to stop)").upper().strip()[0]
        if r_c == '0':
            break
        while r_c not in mapping:
            r_c = input("That character does not exist in the ciphertext, try a different character").upper().strip()[0]
             
        r_c2 = input("what character do you want to replace it with? ").upper().strip()[0]

        for k,v in mapping.items():
            if v == r_c2:
                # this ensures that the mapping that gets replaced does not get lost
                mapping[k] = mapping[r_c]
                break
        
        # replaces the original mapping with the true mapping that the user just provided
        mapping[r_c] = r_c2

        print("\nOriginal ciphertext:")
        print(ciphertext)

        print("\nHere is the new plaintext:")
        print(decode(ciphertext, mapping))
        


