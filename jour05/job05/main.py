#Simple cesar cipher, not handling special characters
def cesar(sentence, code):
    codedsentence = ""
    for e in sentence:
        #Handling spaces
        if ord(e) == 32:
            codedsentence+="a"
        else:
            codedsentence += chr((ord(e)+(ord(code)-96))%123)
    print(codedsentence)

cesar("Salut a tous", "a")
