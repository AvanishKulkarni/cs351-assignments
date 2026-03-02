from collections import Counter

def decode(ciphertext, mapping):
    # decode the ciphertext using the mapping
    decoded = ""
    for c in ciphertext:
        if c.isalpha():
            decoded += mapping[c.lower()]
        else:
            decoded += c

    return decoded

if __name__ == "__main__":

    # clean user input to alphabetic only
    ciphertext = input("Enter ciphertext:\n")
    clean = "".join(c.lower() for c in ciphertext if c.isalpha())

    # get letters ordered by freq
    count = Counter(clean).most_common()
    freq, _ = zip(*count)

    # map frequencies to known English letter frequencies
    # source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    eng_freq = ['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

    # create mapping from ciphertext letters to English letters
    mapping = {c.lower(): e.lower() for c, e in zip(freq, eng_freq)}
    
    print(decode(ciphertext, mapping))

    # ask user to refine mapping if needed
    while True:
        r_c = input("What character do you want to replace? (type 0 to stop)").lower().strip()[0]   
        if r_c == '0':
            break
             
        r_c2 = input("what character do you want to replace it with? ").lower().strip()[0]

        for k,v in mapping.items():
            if v == r_c2:
                mapping[k] = mapping[r_c]
                break

        mapping[r_c] = r_c2

        print("\nOriginal ciphertext:")
        print(ciphertext)

        print("\nHere is the new plaintext:")
        print(decode(ciphertext, mapping))
        


