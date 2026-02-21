from collections import Counter

if __name__ == "__main__":

    # clean user input to alphabetic only
    ciphertext = input("Enter ciphertext: ")
    clean = "".join(c.lower() for c in ciphertext if c.isalpha())

    # get letters ordered by freq
    count = Counter(clean).most_common()
    freq, _ = zip(*count)

    # map frequencies to known English letter frequencies
    # source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    eng_freq = ['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

    guess = zip([freq, eng_freq]) # this will truncate, TODO fix

    print(guess)

