from random import *
def luke(listenotes):
    for i in range(len(listenotes)):
        if listenotes[i] < 40:
            listenotes[i] = f"{listenotes[i]} échoué"
        elif listenotes[i]%5 >= 3:
                listenotes[i] = 5*(listenotes[i] // 5) + 5
    return(listenotes)

randomnotes = [randint(0, 100) for i in range(20)]
print(randomnotes)
print(luke(randomnotes))