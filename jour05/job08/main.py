import random

#Here using a bubble sort algorithm
def bubble(liste):
    coups = 0
    #For each index of the list...
    for i in range(len(liste)):
        #...we go through each index of the list between 0 and the indexes
        #already sorted, meaning the largest number is already at the end position
        for j in range(0, len(liste) - i - 1):
            if liste[j] > liste[j+1]:
                coups += 1
                liste[j], liste[j+1] = liste[j+1], liste[j]
    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")
    print(f"Liste triée : {liste}")
L = [random.randint(0, 2000) for i in range(100)]
print(L)
bubble(L)
