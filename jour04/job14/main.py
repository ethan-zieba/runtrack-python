def my_long_word(n, sentence):
    wordlist = sentence.split(" ")
    print(wordlist)
    validwords = []
    for e in wordlist:
        wordlength = 0
        for u in e:
            wordlength += 1
        for i in range(wordlength):
            if i > n:
                validwords.append(e)
                break
    print(validwords)

my_long_word(2, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la "
                "colère mène à la haine, la haine mène à la souffrance")
